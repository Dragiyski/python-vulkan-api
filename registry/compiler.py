import re
import os
import ctypes
from collections import OrderedDict
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines, PythonCode
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CPointerType, CComplexType, CArrayType, CFunctionType, CHandleType
from .context import Context, NameMap, Alias
from .cparser import CParser

class CCode(pycparser.c_ast.Node):
    __slots__ = ('code')

    def __init__(self, code):
        self.code = code

class CGenerator(pycparser.c_generator.CGenerator):
    def visit_CCode(self, node):
        return node.code
    
class CompilerError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)
    
class CompileNodeError(CompilerError):
    def __init__(self, *args, node: Node, **kwargs):
        super().__init__(f'{node.file_path}:', *args if len(args) > 0 else 'Error while processing node <%s>' % node.node_name, node=node, **kwargs)
    
class DuplicateNodeNameError(CompileNodeError):
    def __init__(self, *args, node: Node, name: str, prev_node: Node, **kwargs):
        super().__init__('Duplicate named node <%s name="%s">, name defined by previous node at %s.' % (node.node_name, name, self.get_node_path(prev_node)), *args, node=node, name=name, prev_node=prev_node, **kwargs)

class MultipleChildrenNodeError(CompileNodeError):
    def __init__(self, *args, node: Node, name: str, count: int, **kwargs):
        super().__init__('Expected node <%s> expected a single child node <%s>, but found %d children.' % (node.node_name, name, count))

class Compiler:
    def __init__(self):
        self.xml_map = OrderedDict()

    def add_xml_file(self, file):
        if (file in self.xml_map):
            raise ValueError('Adding already processed file: %s' % (file))
        root_node = parse_xml(file, is_file=True)
        self.xml_map[file] = root_node

    def _enumerate_tags(self, context: Context, root_node: Node):
        for tags_node in root_node.get_all('tags'):
            for tag_node in tags_node.get_all('tag'):
                if not tag_node.has_attribute('name'):
                    raise CompileNodeError('Expected <tag> node to have a @name attribute.', node=tag_node)
                name = tag_node.get_attribute('name')
                context.tag_set.add(name)

    # TODO: Check https://github.com/paulross/cpip for full-blown C/C++ preprocessor in python
    def _enumerate_type_nodes(self, context: Context, root_node: Node):
        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                if not context.is_target_api(type_node):
                    continue
                if type_node.has_attribute('alias'):
                    self._enumerate_alias_node(context, type_node)
                else:
                    category = type_node.get_attribute('category')
                    if category == 'define':
                        # defines are not actually a "type", they are just values or formulas.
                        self._enumerate_type_node(context, [category], self.get_node_name, type_node)
                    elif category == 'basetype':
                        self._enumerate_type_node(context, [category, 'all'], self.get_node_name, type_node)
                    elif category is None:
                        self._enumerate_unknown_type(context, type_node)
                    elif category == 'bitmask':
                        self._enumerate_type_node(context, [category, 'set', 'all'], self.get_node_name_from_children, type_node)
                    elif category == 'handle':
                        self._enumerate_type_node(context, ['handle', 'all'], self.get_node_name_from_children, type_node)
                    elif category == 'enum':
                        self._enumerate_type_node(context, [category, 'set', 'all'], self.get_node_name_from_attribute, type_node)
                    elif category == 'struct' or category == 'union':
                        self._enumerate_type_node(context, [category, 'complex', 'all'], self.get_node_name_from_attribute, type_node)
                    elif category == 'funcpointer':
                        self._enumerate_type_node(context, [category, 'all'], self.get_node_name_from_children, type_node)

    @staticmethod
    def get_node_name(node):
        if node.has_attribute('name'):
            return node.get_attribute('name')
        if 'name' in node.children:
            if len(node.children['name']) > 1:
                raise MultipleChildrenNodeError(node=node, name='name', count=len(node.children['name']))
            return node.get('name').get_text()
        raise CompileNodeError('Missing node name: expected either attribute @name or child element <name>', node=node)
    
    @staticmethod
    def get_node_name_from_children(node):
        if 'name' not in node.children:
            raise CompileNodeError('Missing node name: expected child element <name>', node=node)
        if len(node.children['name']) > 1:
            raise MultipleChildrenNodeError(node=node, name='name', count=len(node.children['name']))
        return node.get('name').get_text()
    
    @staticmethod
    def get_node_name_from_attribute(node):
        if not node.has_attribute('name'):
            raise CompileNodeError('Missing node name: expected attribute @name', node=node)
        return node.get_attribute('name')
    
    def _enumerate_alias_node(self, context: Context, node: Node):
        assert node.has_attribute('alias'), "node.has_attribute('alias')"
        alias = node.get_attribute('alias')
        name = self.get_node_name_from_attribute(node)
        if name in context.alias_map:
            if context.alias_map[name] == alias:
                context.alias_map[name].node_set.add(node)
            else:
                raise CompileNodeError('Alias "%s" => "%s" is already defined with different target "%s", previous definitions at %s' % (name, alias, context.alias_map[name], ', '.join(CompileNodeError.get_node_path(prev_node) for prev_node in context.alias_map[name].node_set)))
        context.alias_map[name] = Alias(alias)
        context.alias_map[name].node_set.add(node)

    def _enumerate_type_node(self, context: Context, target_list: list, get_name, node: Node):
        name = get_name(node)
        for target in target_list:
            name_map = context.type_node_map[target]
            try:
                name_map.set(name, node)
            except NameMap.DuplicateKeyError as ex:
                raise DuplicateNodeNameError(node=node, name=name, prev_node=name_map[name]) from ex

    def _enumerate_unknown_type(self, context: Context, node: Node):
        name = self.get_node_name(node)
        if name in context.ctypes_map:
            return
        try:
            context.type_node_map['unknown'].set(name, node)
        except NameMap.DuplicateKeyError as ex:
            raise DuplicateNodeNameError(node=node, name=name, prev_node=context.type_node_map[name])

    def _compile_preprocessor_defines(self, context: Context):
        for name, node in context.type_node_map['define'].items():
            code = node.get_text()
            code = get_preprocessor_lines(code)
            if len(code) != 1:
                continue
            code = code[0]
            func_macro = re.fullmatch(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)', code)
            if func_macro is not None:
                macro_name = func_macro.group(1)
                if macro_name != name:    
                    raise CompilerError('Unable to parse <type category="define" name="%s"> node: #define directive is for different name %s' % (name, macro_name), node=node)
                args = [arg.strip() for arg in func_macro.group(2).split(',')]
                code = func_macro.group(3)
                code = [re.split(r'\b', x) for x in code.split('##')]
                template = []
                for words in code:
                    for word in words:
                        if word in args:
                            if len(template) > 0 and template[-1] == '#':
                                template[-1] = {
                                    'name': word,
                                    'index': args.index(word),
                                    'string': True
                                }
                            else:
                                template.append({
                                    'name': word,
                                    'index': args.index(word),
                                    'string': False
                                })
                        else:
                            template.append(word)
                if name in context.func_macro_map or name in context.object_macro_map:
                    raise CompileNodeError('Duplicate preprocessor #define "%s"' % (name), node=name)
                context.func_macro_map[name] = {
                    'arguments': args,
                    'template': template,
                    'node': node
                }
                continue
            object_macro = re.fullmatch(r'\s*#\s*define\s+(\w+)\s+(.*)', code)
            if object_macro is not None:
                macro_name = object_macro.group(1)
                if macro_name != name:    
                    raise CompileNodeError('Unable to parse <type category="define" name="%s"> node: #define directive is for different name %s' % (name, macro_name), node=node)
                code = object_macro.group(2)
                if name in context.func_macro_map or name in context.object_macro_map:
                    raise CompileNodeError('Duplicate preprocessor #define "%s"' % (name))
                context.object_macro_map[name] = {
                    'code': code,
                    'node': node
                }
                continue
            raise CompilerError('Unable to parse <type category="define" name="%s">: node is not empty, but does not contain function or object macro' % (name), node=node)

    def _resolve_macros(self, context: Context):
        for name, descriptor in context.object_macro_map.items():
            value = context.get_c_constant_value('int', context.object_macro_map[name]['code'])
            descriptor['value'] = value
            context.value_map.set(name, {
                'node': descriptor['node'],
                'value': value
            })
        for name, descriptor in context.func_macro_map.items():
            node = context.get_python_code_for_func_macro(name)
            if node is not None:
                descriptor['python_node'] = node

    def _compile_basetype_node_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.type_node_map['basetype'].items():
            if name in context.ctypes_map:
                return
            words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in node.get_text_nodes_before(node.get('name'))]))]
            words = [x for x in words if x]
            if 'typedef' not in words:
                if words[-1] == 'struct':
                    context.ctypes_map[name] = CType()
                    continue
                raise CompilerError('Basetype "%s" not a typedef or struct' % (name), node=node)
            words = words[len(words) - words[::-1].index('typedef'):]
            ctype = ' '.join(words).strip()
            ptr_count = 0
            while ctype.endswith('*'):
                ctype = ctype[:-1].strip()
                ptr_count += 1
            if 'struct' in words or 'union' in words:
                ctype = CType()
            elif ctype in context.ctypes_map:
                ctype = context.ctypes_map[ctype]
            else:
                raise CompilerError('Basetype "%s" is a typedef to an unknown type "%s"' % (name, ctype), node=node)
            while ptr_count > 0:
                ctype = ctype.pointer()
                ptr_count -= 1
            context.ctypes_map[name] = ctype

    def _enumerate_enum_nodes(self, context: Context, root_node: Node):
        for enums_node in root_node.get_all('enums'):
            if not context.is_target_api(enums_node):
                continue
            enums_name = self.get_node_name_from_attribute(enums_node)
            enums_class = enums_node.get_attribute('type')
            if enums_class is not None and enums_class not in ['enum', 'bitmask']:
                # if enums_class == 'constants':
                enums_class = None
                # else:
                    # raise CompileNodeError('Node <enums name="%s"> unknown enum type "%s"' % (enums_name, enums_class), node=enums_node)
            if enums_class is not None:
                try:
                    context.enums_node_map.set(enums_name, enums_node)
                except NameMap.DuplicateKeyError as ex:
                    raise DuplicateNodeNameError(node=enums_node, name=enums_name, prev_node=context.enums_node_map[enums_name])
            for enum_node in enums_node.get_all('enum'):
                if not context.is_target_api(enum_node):
                    continue
                enum_name = self.get_node_name_from_attribute(enum_node)
                if enum_node.has_attribute('alias'):
                    self._enumerate_alias_node(context, enum_node)
                    continue
                enum_object = { 'enum_node': enum_node, 'enums_node': enums_node }
                if enums_class is not None:
                    enum_object['enum_class'] = enums_class
                    enum_object['enum_name'] = enums_name
                if enum_node.has_attribute('type'):
                    enum_object['type'] = enum_node.get_attribute('type')
                try:
                    context.enum_node_map.set(enum_name, enum_object)
                except NameMap.DuplicateKeyError as ex:
                    raise DuplicateNodeNameError(node=enum_node, name=enum_name, prev_node=context.enum_node_map[enum_name])
                
    
    def _enumerate_command_nodes(self, context: Context, root_node: Node):
        for commands_node in root_node.get_all('commands'):
            for command_node in commands_node.get_all('command'):
                if not context.is_target_api(command_node):
                    continue
                if command_node.has_attribute('alias'):
                    self._enumerate_alias_node(context, command_node)
                    continue
                if 'proto' not in command_node.children:
                    raise CompileNodeError('Missing child <proto> for <command> node', node=command_node)
                if len(command_node.children['proto']) > 1:
                    raise MultipleChildrenNodeError(node=command_node, name='proto', count=len(command_node.children['proto']))
                proto_node = command_node.get('proto')
                name = self.get_node_name_from_children(proto_node)
                try:
                    context.command_node_map.set(name, command_node)
                except NameMap.DuplicateKeyError as ex:
                    raise DuplicateNodeNameError(node=command_node, name=name, prev_node=context.command_node_map[name]) from ex
    
    def _compile_handle_node_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.type_node_map['handle'].items():
            typedef = node.get('type').get_text()
            # One of [VK_NULL_HANDLE, VK_DEFINE_NON_DISPATCHABLE_HANDLE]
            ctype = CHandleType(name)
            if name in context.ctypes_map:
                raise CompileNodeError('Handle node type "%s" already defined as %r' % (name, context.ctypes_map[name]), node=node)
            context.ctypes_map[name] = ctype
            descriptor = { 'ctype': ctype, 'typedef': typedef }
            if node.has_attribute('parent'):
                descriptor['parent'] = node.get_attribute('parent')
            context.handle_map.set(name, descriptor)

    def _compile_bitmask_node_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.type_node_map['bitmask'].items():
            descriptor = { 'class': 'bitmask', 'values': set(), 'type_node': node }
            if 'type' not in node.children:
                raise CompileNodeError('Missing child <type> for node <type category="%s" name="%s">' % (node.get_attribute('category'), name), node=node)
            if len(node.children['type']) > 1:
                raise MultipleChildrenNodeError(node=node, name='type', count=len(node.children['type']))
            ctype_name = node.get('type').get_text()
            if ctype_name not in context.ctypes_map:
                raise CompileNodeError('Node <type category="%s" name="%s"> use unknown type "%s"' % (node.get_attribute('category'), name, ctype_name), node=node)
            descriptor['type'] = ctype_name
            descriptor['ctype'] = context.ctypes_map[ctype_name]
            ctype = context.ctypes_map[ctype_name]
            if name in context.ctypes_map:
                raise CompileNodeError('Node <type category="%s" name="%s"> with type "%s" already defined in ctypes as %r' % (node.get_attribute('category'), name, ctype_name, context.ctypes_map[name]), node=node)
            context.ctypes_map[name] = ctype
            bit_name = None
            if node.has_attribute('bitvalues'):
                bit_name = node.get_attribute('bitvalues')
            elif node.has_attribute('requires'):
                bit_name = node.get_attribute('requires')
            if bit_name is not None:
                try:
                    context.bit_map.set(bit_name, name)
                except NameMap.DuplicateKeyError as ex:
                    raise CompileNodeError('Bitmask "%s" assigns "%s" enum, already assigned by another bitmask "%s"' % (name, bit_name, context.bit_map[bit_name]), node=node) from ex
                descriptor['bit_name'] = bit_name
                if bit_name in context.ctypes_map:
                    if context.ctypes_map[bit_name] is not context.ctypes_map[name]:
                        raise CompileNodeError('Attempt to reassign bit values "%s" to different type than their bitmask "%s"' % (bit_name, name), node=node)
                else:
                    context.ctypes_map[bit_name] = context.ctypes_map[name]
            try:
                context.enum_map.set(name, descriptor)
            except NameMap.DuplicateKeyError as ex:
                raise DuplicateNodeNameError(node=node, name=name, prev_node=context.enum_map[name])
            
    def _compile_enum_node_map(self, context: Context):
        for name, node in context.enums_node_map.items():
            if name in context.bit_map:
                continue
            descriptor = { 'class': 'enum', 'values': set(), 'type_node': node }
            ctype = context.ctypes_map['int']
            if name in context.ctypes_map:
                if context.ctypes_map[name] is not ctype:
                    raise CompileNodeError('Attempt to reassign the type of enum "%s"' % (name), node=node)
                ctype = context.ctypes_map[name]
            else:
                context.ctypes_map[name] = ctype
            descriptor['ctype'] = ctype
            context.enum_map[name] = descriptor
    
    def _get_enum_value(self, context: Context, node: Node):
        if node.has_attribute('bitpos'):
            bitpos = context.cparser.parse_c_int(node.get_attribute('bitpos'))
            return 1 << bitpos
        if node.has_attribute('value'):
            value = context.get_c_constant_value('int', node.get_attribute('value'))
            return value
        raise CompileNodeError('Missing enum value: Neither @value, nor @bitpos pressent', node=node)

    def _compile_enum_values(self, context: Context):
        for name, enum_descriptor in context.enum_node_map.items():
            enum_node = enum_descriptor['enum_node']
            if 'type' not in enum_descriptor:
                if 'enum_name' not in enum_descriptor:
                    raise CompileNodeError('A constant "%s" missing @type attribute' % name, name=name, node=enum_node)
                ctype_name = enum_descriptor['enum_name']
            else:
                ctype_name = enum_descriptor['type']
            if ctype_name not in context.ctypes_map:
                    raise CompileNodeError('An enum/constant "%s" defined as unknown ctype "%s"' % (name, ctype_name), node=enum_node)
            descriptor = { 'node': enum_node, 'type': ctype_name, 'value': self._get_enum_value(context, enum_node), 'ctype': context.ctypes_map[ctype_name] }
            if 'enum_name' in enum_descriptor:
                if 'enum_class' not in enum_descriptor or enum_descriptor['enum_class'] not in ['enum', 'bitmask']:
                    raise CompileNodeError('An enum "%s" not has enum_class, but no enum_name.' % (name), node=enum_node)
                enum_name = enum_descriptor['enum_name']
                if enum_name in context.bit_map:
                    enum_name = context.bit_map[enum_name]
                if enum_name not in context.enum_map:
                    raise CompileNodeError('An enum value "%s" defined as part of non-existing enum "%s"' % (name, enum_name), node=enum_node)
                context.enum_map[enum_name]['values'].add(name)
                descriptor['enum_name'] = enum_name
                descriptor['enum_class'] = enum_descriptor['enum_class']
            context.value_map.set(name, descriptor)
    
    def _get_feature_enum_value(self, context: Context, enum_node: Node, feature_node: Node):
        enum_name = self.get_node_name_from_attribute(enum_node)
        feature_name = self.get_node_name_from_attribute(feature_node)
        if enum_node.has_attribute('offset'):
            if enum_node.has_attribute('extnumber'):
                ext_number = enum_node.get_attribute('extnumber')
            else:
                raise CompileNodeError('Feature "%s", enum "%s" is defined as @offset, but missing extension number' % (self.make_path(enum_node), feature_name, enum_name))
            offset = context.cparser.parse_c_int(enum_node.get_attribute('offset'))
            ext_offset = (context.cparser.parse_c_int(ext_number) - 1) * 1000
            base = 1000000000
            value = base + ext_offset + offset
        elif enum_node.has_attribute('value') or enum_node.has_attribute('bitpos'):
            value = self._get_enum_value(context, enum_node)
        else:
            return None
        if enum_node.get_attribute('dir') == '-':
            value = -value
        return value

    def _compile_feature_nodes(self, context: Context):
        root_node: Node
        for root_node in self.xml_map.values():
            for feature_node in root_node.get_all('feature'):
                if not context.is_target_api(feature_node):
                    continue
                feature_name = self.get_node_name_from_attribute(feature_node)
                try:
                    context.feature_map.set(feature_name, {
                        'node': feature_node,
                        'values': set(),
                        'types': set(),
                        'commands': set(),
                    })
                except NameMap.DuplicateKeyError as ex:
                    raise DuplicateNodeNameError(node=feature_node, name=feature_name, prev_node=context.feature_map[feature_name]['node']) from ex
                if feature_node.has_attribute('number'):
                    version = feature_node.get_attribute('number').split('.')
                    is_version = True
                    try:
                        version = [int(n) for n in version]
                    except ValueError:
                        is_version = False
                    if is_version:
                        context.feature_map[feature_name]['version'] = version
                # Depends: Introduce dependencies:
                # This is AND-OR tree in format:
                # A + B means A AND B
                # A, B means A OR B
                # (...) grouping expression (brackets)
                # and can include both extension and features.
                # Some extension will be deprecated, if they move to a vulkan version.
                # For example: VK_KHR_video_queue depends on VK_VERSION_1_1 and VK_KHR_synchronization2, or VK_VERSION_1_3, because
                # VK_KHR_synchronization2 has been promoted to VK_VERSION_1_3.
                for require_node in feature_node.get_all('require'):
                    if not context.is_target_api(require_node):
                        continue
                    for enum_node in require_node.get_all('enum'):
                        if not context.is_target_api(enum_node):
                            continue
                        enum_name = self.get_node_name_from_attribute(enum_node)
                        context.feature_map[feature_name]['values'].add(enum_name)
                        if enum_node.has_attribute('alias'):
                            self._enumerate_alias_node(context, enum_node)
                            continue
                        extend_name = None
                        if enum_node.has_attribute('extends'):
                            type_name = extend_name = enum_node.get_attribute('extends')
                            if extend_name in context.bit_map:
                                extend_name = context.bit_map[extend_name]
                            if extend_name not in context.enum_map:
                                raise CompileNodeError('Feature "%s", constant "%s": Extending non-existent enum "%s"' % (feature_name, enum_name, extend_name), node=enum_node)
                        if extend_name is None:
                            continue
                        descriptor = {
                            'node': enum_node,
                            'value': self._get_feature_enum_value(context, enum_node, feature_node),
                            'enum_name': extend_name,
                            'enum_class': context.enum_map[extend_name]['class'],
                            'type': type_name
                        }
                        descriptor['value'] = self._get_feature_enum_value(context, enum_node, feature_node)
                        if descriptor['value'] is None:
                            if enum_name not in context.value_map:
                                raise CompileNodeError('Feature "%s" requires constant "%s" value, but it is not defined.' % (feature_name, enum_name), node=enum_node)
                            continue
                        else:
                            if type_name not in context.ctypes_map:
                                raise CompileNodeError('Feature "%s" attempts to extend enum "%s", but the enum is unknown ctype "%s"' % (feature_name, extend_name, type_name), node=enum_node)
                            descriptor['ctype'] = context.ctypes_map[type_name]
                        if enum_name in context.value_map:
                            if context.value_map[enum_name]['value'] != descriptor['value']:
                                raise CompileNodeError('Feature "%s", enum "%s" = (%r) is already defined in value map with different value (%r)' % (feature_name, enum_name, descriptor['value'], context.value_map[enum_name]), node=enum_node)
                        else:
                            context.value_map.set(enum_name, descriptor)
                        context.enum_map[extend_name]['values'].add(enum_name)
                    for type_node in require_node.get_all('type'):
                        type_name = self.get_node_name_from_attribute(type_node)
                        if type_name in context.object_macro_map:
                            if type_name not in context.value_map:
                                raise CompileNodeError('Feature "%s", requires type "%s" which is defined as object macro, but not found in the value map.' % (feature_name, enum_name), node=type_node)
                            context.feature_map[feature_name]['values'].add(type_name)
                            continue
                        context.feature_map[feature_name]['types'].add(type_name)
                    for command_node in require_node.get_all('command'):
                        command_name = self.get_node_name_from_attribute(command_node)
                        context.feature_map[feature_name]['commands'].add(command_name)
    
    def _get_ext_enum_value(self, context: Context, enum_node: Node, ext_node: Node):
        enum_name = self.get_node_name_from_attribute(enum_node)
        ext_name = self.get_node_name_from_attribute(ext_node)
        if enum_node.has_attribute('offset'):
            if enum_node.has_attribute('extnumber'):
                ext_number = enum_node.get_attribute('extnumber')
            elif ext_node.has_attribute('number'):
                ext_number = ext_node.get_attribute('number')
            else:
                raise CompileNodeError('In extension "%s", enum "%s" is defined as @offset, but missing extension number' % (ext_name, enum_name), node=enum_node)
            offset = context.cparser.parse_c_int(enum_node.get_attribute('offset'))
            ext_offset = (context.cparser.parse_c_int(ext_number) - 1) * 1000
            base = 1000000000
            value = base + ext_offset + offset
        elif enum_node.has_attribute('value') or enum_node.has_attribute('bitpos'):
            value = self._get_enum_value(context, enum_node)
        else:
            return None
        if enum_node.get_attribute('dir') == '-':
            value = -value
        return value

    def _compile_ext_nodes(self, context: Context):
        root_node: Node
        for root_node in self.xml_map.values():
            for extensions_node in root_node.get_all('extensions'):
                if not context.is_target_api(extensions_node):
                    continue
                for ext_node in extensions_node.get_all('extension'):
                    if not context.is_target_api(ext_node):
                        continue
                    if ext_node.has_attribute('supported'):
                        supported = ext_node.get_attribute('supported')
                        if supported == 'disabled':
                            continue
                        if not context.is_target_api_value(supported):
                            continue
                    ext_name = self.get_node_name_from_attribute(ext_node)
                    context.ext_map.set(ext_name, {
                        'node': ext_node,
                        'values': set(),
                        'types': set(),
                        'commands': set(),
                    })
                    # Depends: Introduce dependencies:
                    # This is AND-OR tree in format:
                    # A + B means A AND B
                    # A, B means A OR B
                    # (...) grouping expression (brackets)
                    # and can include both extension and features.
                    # Some extension will be deprecated, if they move to a vulkan version.
                    # For example: VK_KHR_video_queue depends on VK_VERSION_1_1 and VK_KHR_synchronization2, or VK_VERSION_1_3, because
                    # VK_KHR_synchronization2 has been promoted to VK_VERSION_1_3.

                    # Note: We cannot create a module containing all values for this extension and its dependencies, as this could include features.
                    # Instead, create a module that include the bare minimum.
                    for require_node in ext_node.get_all('require'):
                        if not context.is_target_api(require_node):
                            continue
                        for enum_node in require_node.get_all('enum'):
                            if not context.is_target_api(enum_node):
                                continue
                            enum_name = self.get_node_name_from_attribute(enum_node)
                            context.ext_map[ext_name]['values'].add(enum_name)
                            if enum_node.has_attribute('alias'):
                                self._enumerate_alias_node(context, enum_node)
                                continue
                            descriptor = {
                                'node': enum_node,
                                'value': self._get_ext_enum_value(context, enum_node, ext_node)
                            }
                            if descriptor['value'] is None:
                                continue
                            extend_name = None
                            if enum_node.has_attribute('extends'):
                                type_name = extend_name = enum_node.get_attribute('extends')
                                if extend_name in context.bit_map:
                                    extend_name = context.bit_map[extend_name]
                                if extend_name not in context.enum_map:
                                    raise CompileNodeError('Extension "%s", enum "%s": Extending non-existent enum "%s"' % (ext_name, enum_name, extend_name), node=enum_node)
                            if extend_name is not None:
                                if type_name not in context.ctypes_map:
                                    raise CompileNodeError('In extesnion "%s" attempts to extend enum "%s", but the enum is unknown ctype "%s".' % (ext_name, extend_name, type_name), node=enum_node)
                                descriptor['type'] = type_name
                                descriptor['ctype'] = context.ctypes_map[extend_name]
                                context.enum_map[extend_name]['values'].add(enum_name)
                            if enum_name in context.value_map:
                                if context.value_map[enum_name]['value'] != descriptor['value']:
                                    raise CompileNodeError('In extension "%s", enum "%s" = (%r) is already defined in value map with different value (%r)' % (ext_name, enum_name, descriptor['value'], context.value_map[enum_name]), node=enum_node)
                            else:
                                context.value_map.set(enum_name, descriptor)
                        for type_node in require_node.get_all('type'):
                            type_name = self.get_node_name_from_attribute(type_node)
                            if type_name in context.object_macro_map:
                                if type_name not in context.value_map:
                                    raise CompileNodeError('Feature "%s", requires type "%s" which is defined as object macro, but not found in the value map.' % (ext_name, enum_name), node=type_node)
                                context.ext_map[ext_name]['values'].add(type_name)
                                continue
                            context.ext_map[ext_name]['types'].add(type_name)
                        for command_node in require_node.get_all('command'):
                            command_name = self.get_node_name_from_attribute(command_node)
                            context.ext_map[ext_name]['commands'].add(command_name)

    def _compile_callback_node_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.type_node_map['funcpointer'].items():
            if not name.startswith('PFN_'):
                raise CompileNodeError('Expected callback name to be function pointer named starting with PFN_', node=node)
            fn_type = context.ctypes_map[name[4:]] = CFunctionType(name[4:])
            context.ctypes_map[name] = fn_type

    def _compile_uncategorized_types(self, context: Context):
        # While it is an error to use uncategorized type, it is not an error to use a pointer to uncategorized type.
        # Pointer to uncategorized types are pointer to black-box structures, thus handled as void*.
        for name in context.type_node_map['unknown']:
            if name not in context.ctypes_map and name not in context.type_node_map['complex']:
                context.ctypes_map[name] = CType()
    
    def _compile_complex_types(self, context: Context):
        for name, node in context.type_node_map['complex'].items():
            self._compile_complex_type(context, name, node)

    def _get_member_code(self, context: Context, node: Node):
        code = []
        child: Node
        for child in node.child_nodes:
            if child.node_name == 'comment':
                continue
            if child.node_name == 'enum':
                enum_name = child.get_text()
                if enum_name not in context.value_map:
                    raise CompileNodeError('Reference to unknown enum "%s"' % (enum_name), node=node)
                enum_value = context.value_map[enum_name]['value']
                if isinstance(enum_value, str):
                    enum_value = context.cparser.generate_c_string(enum_value)
                else:
                    assert isinstance(enum_value, int) or isinstance(enum_value, float), 'isinstance(enum_value, int) or isinstance(enum_value, float)'
                    enum_value = str(enum_value)
                code.append(enum_value)
                continue
            code.append(child.get_text())
        return ''.join(code)
    
    @staticmethod
    def _process_len_attribute(target: dict, node: Node):
        # If the len value is computed, it must be handled manually
        target['is_string'] = False
        if node.has_attribute('len'):
            length = node.get_attribute('len')
            if 'latexmath' in length:
                target['length_need_processor'] = None
                if node.has_attribute('altlen'):
                    target['length_need_processor'] = node.get_attribute('altlen')
                    return
            length = [s.strip() for s in length.split(',')]
            if length[-1] == 'null-terminated':
                target['is_string'] = True
                length = length[:-1]
            for i, entry in enumerate(length):
                try:
                    entry = int(entry, base=10)
                except ValueError:
                    entry = entry.split('->')
                length[i] = entry
            target['length'] = length
    
    def _resolve_complex_type(self, context: Context, name: str, node: Node):
        assert name in context.ctypes_map, 'name in context.ctypes_map'
        ctype = context.ctypes_map[name]
        assert isinstance(ctype, CComplexType), 'isinstance(ctype, CComplexType)'
        keyword = 'union' if node.get_attribute('category') == 'union' else 'struct'
        code = [
            '%s %s {' % (keyword, name)
        ]
        for member_node in node.get_all('member'):
            if not context.is_target_api(member_node):
                continue
            code.append('    %s;' % self._get_member_code(context, member_node))
        code.append('};')
        code = '\n'.join(code)
        code = context.preprocess_c_code(code)
        ast = context.cparser.parse(code)
        assert len(ast.ext) == 1, 'len(ast.ext) == 1'
        assert type(ast.ext[0]) is pycparser.c_ast.Decl, 'type(ast.ext[0]) is pycparser.c_ast.Decl'
        assert type(ast.ext[0].type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union], 'type(ast.ext[0].type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union]'
        assert ast.ext[0].type.name == name, 'ast.ext[0].type.name == name'
        for decl in ast.ext[0].type.decls:
            type_decl = decl.type
            member_type = context.get_type_from_decl(type_decl)
            assert decl.name in ctype.member_map, 'decl.name in ctype.member_map'
            ctype.member_map[decl.name]['ctype'] = member_type
            if decl.bitsize is not None:
                if type(decl.bitsize) is not pycparser.c_ast.Constant:
                    raise CompileNodeError('In struct %s, member %s: bitsize is not specified as constant' % (name, decl.name), node=member_node)
                bitsize = context.get_c_ast_const_value(decl.bitsize)
                if not isinstance(bitsize, int):
                    raise CompileNodeError('In struct %s, member %s: bitsize is not an integer constant' % (name, decl.name), node=member_node)
                ctype.member_map[decl.name]['bitsize'] = bitsize
        for member_name in ctype.member_list:
            member_desc = ctype.member_map[member_name]
            member_node = member_desc['node']
            member_node: Node
            member_ctype = member_desc['ctype']
            if member_node.has_attribute('values'):
                values = [value.strip() for value in member_node.get_attribute('values').split(',')]
                if member_name == 'sType' and (len(values) != 1 or not values[0].startswith('VK_STRUCTURE_TYPE_')):
                    raise CompileNodeError('Invalid @values attribute for structure type "sType" in "%s", expected a single value starting with "VK_STRUCTURE_TYPE_"' % name, node=member_node)
                if len(values) == 1:
                    member_desc['value'] = values[0]
                else:
                    member_desc['values'] = values
            self._process_len_attribute(member_desc, member_node)
            if member_node.has_attribute('externsync'):
                member_externsync = [s.strip() for s in member_node.get_attribute('externsync').split(',')]
                member_externsync = [s.split('->') for s in member_externsync]
                if len(member_externsync) > 0:
                    member_desc['externsync'] = member_externsync
            member_desc['is_enum'] = 'type' in member_desc and member_desc['type'] in context.enum_map

    def _compile_complex_type(self, context: Context, name: str, node: Node):
        if name in context.ctypes_map:
            assert isinstance(context.ctypes_map[name], CComplexType), 'isinstance(context.ctypes_map[name], CComplexType)'
            return
        if name in context.resolving_complex_type:
            return
        context.resolving_complex_type.add(name)
        try:
            # Step 1: Add ctype to ctypes_map immediately, so we know we have such type
            constructor = 'Union' if node.get_attribute('category') == 'union' else 'Structure'
            ctype = context.ctypes_map[name] = CComplexType(name, constructor)
            # Step 2: Resolve the fields, this might recursively call into _compile_complex_type
            ctype['delay_fields'] = False
            ctype['dependencies'] = []
            ctype['node'] = node
            include_struct = set()
            for member_node in node.get_all('member'):
                if not context.is_target_api(member_node):
                    continue
                member_name = self.get_node_name_from_children(member_node)
                ctype.member_map[member_name] = {'node': member_node, 'python_name': context.make_python_name(member_name), 'is_string': False}
                ctype.member_list.append(member_name)
                if 'type' not in member_node.children:
                    raise CompileNodeError('Member "%s.%s": Missing attribute @type' % (name, member_name), node=member_node)
                if len(member_node.children['type']) > 1:
                    raise MultipleChildrenNodeError(node=member_node, name='type', count=len(member_node.children['type']))
                member_type = context.resolve_alias(member_node.get('type').get_text())
                if member_type in context.type_node_map['set'] or member_type in context.type_node_map['complex']:
                    ctype['dependencies'].append(member_type)
                    ctype.member_map[member_name]['type'] = member_type
                if member_type in context.type_node_map['complex']:
                    include_struct.add(member_type)
                if member_type in context.resolving_complex_type:
                    assert member_type in context.ctypes_map, 'member_type in context.ctypes_map'
                    assert member_type in context.type_node_map['complex'], """member_type in context.type_node_map['complex']"""
                    assert isinstance(context.ctypes_map[member_type], CComplexType), 'isinstance(context.ctypes_map[member_type], CComplexType)'
                    ctype['delay_fields'] = True
                elif member_type not in context.ctypes_map:
                    if member_type in context.type_node_map['complex']:
                        self._compile_complex_type(context, member_type, context.type_node_map['complex'][member_type])
                        assert member_type in context.ctypes_map, 'member_type in context.ctypes_map'
                    else:
                        # Foreign types must have been resolved at this time (see category="basetype")
                        raise CompileNodeError('Member "%s.%s": Reference to unknow type "%s"' % (name, member_name, member_type))
            self._resolve_complex_type(context, name, node)
            descriptor = { 'type': name, 'ctype': ctype, 'extends': set(), 'extended_by': set(), 'included_in': set(), 'includes': include_struct, 'input_of': set(), 'output_of': set(), 'node': node }
            context.struct_map.set(name, descriptor)
        finally:
            context.resolving_complex_type.remove(name)
    
    def _resolve_callback_type_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.type_node_map['funcpointer'].items():
            code = self._get_member_code(context, node)
            code = re.sub(r'\bVKAPI_PTR\b', '', code)
            code = context.preprocess_c_code(code)
            ast = context.cparser.parse(code)
            assert type(ast.ext[0]) == pycparser.c_ast.Typedef, 'type(ast.ext[0]) == pycparser.c_ast.Typedef'
            assert ast.ext[0].name == name, 'ast.ext[0].name == name'
            assert type(ast.ext[0].type == pycparser.c_ast.PtrDecl), 'type(ast.ext[0].type == pycparser.c_ast.PtrDecl)'
            assert type(ast.ext[0].type.type == pycparser.c_ast.FuncDecl), 'type(ast.ext[0].type.type == pycparser.c_ast.FuncDecl)'
            assert name.startswith('PFN_'), "name.startswith('PFN_')"
            assert name in context.ctypes_map, 'name in self.ctypes_map'
            assert name[4:] in context.ctypes_map, 'name[4:] in self.ctypes_map'
            assert context.ctypes_map[name[4:]] is context.ctypes_map[name]
            fn_decl = ast.ext[0].type.type
            ctype = context.ctypes_map[name[4:]]
            assert isinstance(ctype, CFunctionType), 'isinstance(ctype, CFunctionType)'
            ctype.constructor = 'VKAPI_PTR'
            callback_info = {
                'name': name,
                'node': node,
                'ctype': ctype,
                'arg_list': [],
                'arg_map': {}
            }
            for param in fn_decl.args.params:
                param_ctype = context.get_type_from_decl(param.type)
                ctype.argument_types.append(param_ctype)
                callback_info['arg_list'].append(param.name)
                callback_info['arg_map'][param.name] = param_ctype
                if param.name == 'pUserData':
                    ctype['user_data'] = len(ctype.argument_types) - 1
            if len(ctype.argument_types) == 1 and ctype.argument_types[0] is context.ctypes_map['void']:
                ctype.argument_types.pop()
                callback_info['arg_map'].clear()
                callback_info['arg_list'].clear()
            return_ctype = context.get_type_from_decl(fn_decl.type)
            callback_info['return'] = return_ctype
            context.callback_map.set(name, callback_info)
            ctype.return_type = return_ctype

    def _compile_commands(self, context: Context):
        name: str
        node: Node
        for name, node in context.command_node_map.items():
            if not context.is_target_api(node):
                continue
            code = '%s(%s);' % (self._get_member_code(context, node.get('proto')), ', '. join([self._get_member_code(context, x) for x in node.get_all('param') if context.is_target_api(x)]))
            code = context.preprocess_c_code(code)
            ast = context.cparser.parse(code)
            assert type(ast.ext[0]) == pycparser.c_ast.Decl, 'type(ast.ext[0]) == pycparser.c_ast.Decl'
            assert type(ast.ext[0].type == pycparser.c_ast.FuncDecl), 'type(ast.ext[0].type == pycparser.c_ast.FuncDecl)'
            decl = ast.ext[0].type
            ctype = CFunctionType(name)
            ctype['name'] = name
            ctype['node'] = node
            ctype.constructor = 'VKAPI_CALL'
            ctype.return_type = context.get_type_from_decl(decl.type)
            for param in decl.args.params:
                param_ctype = context.get_type_from_decl(param.type)
                ctype.argument_types.append(param_ctype)
            if len(ctype.argument_types) == 1 and ctype.argument_types[0] is context.ctypes_map['void']:
                ctype.argument_types.pop()
            if name in context.ctypes_map:
                raise CompileNodeError('Command "%s" already is context.ctypes' % (name), node=node)
            context.ctypes_map[name] = ctype

    def _compile_plain_ctypes(self, context: Context):
        ctype_name_map = { name: getattr(ctypes, name) for name in dir(ctypes) if name.startswith('c_') and isinstance(getattr(ctypes, name), type) }
        ctype_pytype_map = { ctype: type(ctype().value) for ctype in set(ctype_name_map.values()) }
        ctype_numeric_map = { ctype: pytype for ctype, pytype in ctype_pytype_map.items() if pytype in [int, float] }
        ctype_int_map = { ctype: pytype for ctype, pytype in ctype_pytype_map.items() if pytype is int }
        classname_map = { k: v.__name__[2:] for k, v in ctype_name_map.items() }
        for ctype_name, class_name in classname_map.items():
            cap_count = 2 if class_name.startswith('u') else 1
            class_name = class_name[:cap_count].upper() + class_name[cap_count:]
            for capitalize_word in ['double', 'long']:
                word_cap = class_name.find(capitalize_word)
                if word_cap >= 0:
                    class_name = class_name[:word_cap] + class_name[word_cap].upper() + class_name[word_cap+1:]
            if class_name.endswith('_p'):
                class_name = class_name[:-2] + 'Pointer'
            classname_map[ctype_name] = class_name
        for ctype, pytype in ctype_int_map.items():
            class_name = classname_map[ctype.__name__]
            context.plain_ctype_class['enum'][ctype] = { 'class_name': f'Vulkan{class_name}Enum', 'python_type': pytype.__name__, 'base_class_name': 'IntEnum' }
            context.plain_ctype_class['bitmask'][ctype] = { 'class_name': f'Vulkan{class_name}Flag', 'python_type': pytype.__name__, 'base_class_name': 'IntFlag' }
        for ctype, pytype in ctype_numeric_map.items():
            class_name = classname_map[ctype.__name__]
            context.plain_ctype_class['value'][ctype] = { 'class_name': f'Vulkan{class_name}', 'python_type': pytype.__name__ }
    
    def _compile_struct_extensions(self, context: Context):
        for name, descriptor in context.struct_map.items():
            node = descriptor['node']
            if node.has_attribute('structextends'):
                extends = [context.resolve_alias(s.strip()) for s in node.get_attribute('structextends').split(',')]
                for extend in extends:
                    if extend not in context.struct_map:
                        raise CompileNodeError('Attribute @structextends refers to non-existent struct "%s".' % extend, node=node)
                    descriptor['extends'].add(extend)
                    context.struct_map[extend]['extended_by'].add(name)

    def _compile_command_nodes(self, context: Context):
        command_node: Node
        for command_name, command_node in context.command_node_map.items():
            command_descriptor = { 'argument_list': [], 'argument_map': NameMap(), 'ctype': context.ctypes_map[command_name] }
            return_type = context.resolve_alias(command_node.get('proto').get('type').get_text())
            return_descriptor = { 'type': return_type, 'ctype': context.ctypes_map[return_type] }
            command_descriptor['return'] = return_descriptor
            if return_descriptor['type'] == 'VkResult':
                if command_node.has_attribute('successcodes'):
                    command_descriptor['success_code_list'] = [x for x in [context.resolve_alias(s.strip()) for s in command_node.get_attribute('successcodes').split(',')] if x in context.enum_map['VkResult']['values']]
                else:
                    command_descriptor['success_code_list'] = []
                if command_node.has_attribute('errorcodes'):
                    command_descriptor['error_code_list'] = [x for x in [context.resolve_alias(s.strip()) for s in command_node.get_attribute('errorcodes').split(',')] if x in context.enum_map['VkResult']['values']]
                else:
                    command_descriptor['error_code_list'] = []
            param_node: Node
            param_index = 0
            for param_node in command_node.get_all('param'):
                if not context.is_target_api(param_node):
                    continue
                param_name = param_node.get('name').get_text()
                command_descriptor['argument_list'].append(param_name)
                type_name = context.resolve_alias(param_node.get('type').get_text())
                param_descriptor = { 'type': type_name, 'ctype': command_descriptor['ctype'].argument_types[param_index] }
                self._process_len_attribute(param_descriptor, param_node)
                if param_node.has_attribute('optional'):
                    param_descriptor['optional'] = [s.strip() for s in param_node.get_attribute('optional').split(',')]
                if param_node.has_attribute('externsync'):
                    param_descriptor['externsync'] = param_node.get_attribute('externsync')
                command_descriptor['argument_map'].set(param_name, param_descriptor)
                param_descriptor['output'] = isinstance(param_descriptor['ctype'], CPointerType) and 'const' not in re.split(r'\b', ''.join([node.get_text() for node in param_node.get_text_nodes_before(param_node.get('name'))]))
                if type_name in context.type_node_map['complex']:
                    # Structures given by value or structures given by constant pointer are inputs
                    struct_descriptor = context.struct_map[type_name]
                    struct_key = 'output_of' if param_descriptor['output'] else 'input_of'
                    struct_descriptor[struct_key].add(command_name)
                param_index += 1
            pass
            for param_index, param_name in enumerate(command_descriptor['argument_list']):
                param_descriptor = command_descriptor['argument_map'][param_name]
                if param_descriptor['type'] in context.handle_map and param_descriptor['ctype'] is context.handle_map[param_descriptor['type']]['ctype']:
                    command_descriptor['handle'] = { 'index': param_index, 'type': param_descriptor['type'], 'ctype': param_descriptor['ctype'] }
                    loader_handle = command_descriptor['handle']['type']
                    while loader_handle not in ['VkInstance', 'VkDevice']:
                        loader_handle = context.handle_map[loader_handle]['parent']
                    command_descriptor['handle']['loader'] = loader_handle
                    break
            context.command_map.set(command_name, command_descriptor)

    def _compile_command_names(self, context: Context):
        for command_name in context.command_node_map.keys():
            if not command_name.startswith('vk'):
                continue
            name = command_name[2:]
            words = [tag for tag in context.tag_set if name.endswith(tag)]
            if len(words) > 0:
                name = name[:-len(words[0])]
            words = re.findall(r'[A-Z][a-z0-9]*', name) + words
            context.command_name_map.set(command_name, words)

    def _resolve_inverse_include_struct(self, context: Context):
        for name, descriptor in context.struct_map.items():
            for include_name in descriptor['includes']:
                context.struct_map[include_name]['included_in'].add(name)

    def _filter_api_bug_struct(self, context: Context):
        remove_complex = set()
        remove_funcpointer = set()
        remove_command = set()
        for type_name, node in context.type_node_map['complex'].items():
            for member_node in node.get_all('member'):
                if not context.is_target_api(member_node):
                    continue
                member_name = self.get_node_name_from_children(member_node)
                if member_name == 'sType' and member_node.has_attribute('values'):
                    stype_value = member_node.get_attribute('values')
                    if stype_value not in context.enum_map['VkStructureType']['values']:
                        remove_complex.add(type_name)
        remove_complex_len = len(remove_complex)
        while True:
            for ptr_name, node in context.type_node_map['funcpointer'].items():
                for type_node in node.get_all('type'):
                    fn_type = type_node.get_text()
                    if fn_type in context.type_node_map['complex']:
                        if fn_type in remove_complex:
                            remove_funcpointer.add(ptr_name)
            for type_name, node in context.type_node_map['complex'].items():
                for member_node in node.get_all('member'):
                    if not context.is_target_api(member_node):
                        continue
                    member_type = member_node.get('type').get_text()
                    if member_type in context.type_node_map['complex']:
                        if member_type in remove_complex:
                            remove_complex.add(type_name)
                    if member_type in context.type_node_map['funcpointer']:
                        if member_type in remove_funcpointer:
                            remove_complex.add(type_name)
            if remove_complex_len == len(remove_complex):
                break
            remove_complex_len = len(remove_complex)
        for command_name, command_node in context.command_node_map.items():
            command_types = set(command_node.get('proto').get('type').get_text())
            for param_node in command_node.get_all('param'):
                command_types.add(param_node.get('type').get_text())
            for command_type in command_types:
                if command_type in context.type_node_map['complex']:
                    if command_type in remove_complex:
                        remove_command.add(command_name)
                if command_type in context.type_node_map['funcpointer']:
                    if command_type in remove_funcpointer:
                        remove_command.add(command_name)
        for name in remove_complex:
            del context.type_node_map['complex'][name]
        for name in remove_funcpointer:
            del context.type_node_map['funcpointer'][name]
        for name in remove_command:
            del context.command_node_map[name]

    def compile(self, context = Context()):
        for root_node in self.xml_map.values():
            self._enumerate_tags(context, root_node)
            self._enumerate_type_nodes(context, root_node)
            self._enumerate_enum_nodes(context, root_node)
            self._enumerate_command_nodes(context, root_node)
        self._compile_preprocessor_defines(context)
        self._resolve_macros(context)
        self._compile_basetype_node_map(context)
        self._compile_handle_node_map(context)
        self._compile_bitmask_node_map(context)
        self._compile_enum_node_map(context)
        self._compile_enum_values(context)
        self._compile_feature_nodes(context)
        self._compile_ext_nodes(context)
        self._filter_api_bug_struct(context)
        self._compile_callback_node_map(context)
        self._compile_uncategorized_types(context)
        self._compile_complex_types(context)
        self._resolve_callback_type_map(context)
        self._compile_commands(context)
        self._compile_plain_ctypes(context)
        self._compile_struct_extensions(context)
        self._resolve_inverse_include_struct(context)
        self._compile_command_names(context)
        self._compile_command_nodes(context)
        pass

        return context