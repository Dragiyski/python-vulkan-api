import re
import os
from collections import OrderedDict
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines, PythonCode
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CPointerType, CComplexType, CArrayType, CFunctionType
from .context import Context
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
        super().__init__(f'{self.get_node_path(node)}:', *args if len(args) > 0 else 'Error while processing node <%s>' % node.node_name, node=node, **kwargs)

    @staticmethod
    def get_node_path(node: Node):
        root = node
        while root.parent_node is not None:
            root = root.parent_node
        return f'{root.file}:{node.line}:{node.column}'
    
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
                        self._enumerate_type_define_node(context, type_node)
                    elif category == 'basetype':
                        self._enumerate_type_basetype_node(context, type_node)
                    elif category is None:
                        self._enumerate_uncategorized_type(context, type_node)
                    elif category == 'bitmask':
                        self._enumerate_type_bitmask_node(context, type_node)
                    elif category == 'handle':
                        self._enumerate_type_handle_node(context, type_node)
                    elif category == 'enum':
                        self._enumerate_type_enum_node(context, type_node)
                    elif category == 'struct':
                        self._enumerate_type_struct_node(context, type_node)
                    elif category == 'union':
                        self._enumerate_type_union_node(context, type_node)
                    elif category == 'funcpointer':
                        self._enumerate_type_funcpointer_node(context, type_node)

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
        if not node.has_attribute('alias'):
            raise CompileNodeError('Alias node must have attribute "alias"', node=node)
        assert node.has_attribute('alias'), "node.has_attribute('alias')"
        alias = node.get_attribute('alias')
        name = self.get_node_name_from_attribute(node)
        if name in context.alias_map:
            if context.alias_map[name] != alias:
                raise CompileNodeError('Alias "%s" to "%s" is already defined with different name "%s", previous definitions at: %s' % (name, alias, context.alias_map[name], ', '.join([CompileNodeError.get_node_path(n) for n in context.alias_node_map[name]])), node=node)
        if name not in context.alias_node_map:
            context.alias_node_map[name] = []
        context.alias_node_map[name].append(node)
        context.alias_map[name] = alias

    def _enumerate_type_define_node(self, context: Context, type_node: Node):
        node_name = self.get_node_name(type_node)
        code = type_node.get_text()
        code = get_preprocessor_lines(code)
        if len(code) > 1:
            return
        if len(code) != 1:
            return
        code = code[0]
        func_macro = re.fullmatch(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)', code)
        if func_macro is not None:
            macro_name = func_macro.group(1)
            if macro_name != node_name:    
                raise CompilerError('Unable to parse <type category="define" name="%s"> node: #define directive is for different name %s' % (node_name, macro_name), node=type_node)
            args = [arg.strip() for arg in func_macro.group(2).split(',')]
            code = func_macro.group(3)
            code = [re.split(r'\b', x) for x in code.split('##')]
            template = []
            for words in code:
                for word in words:
                    template.append(word)
            index = 0
            while index < len(template):
                word = template[index]
                if word in args:
                    if index > 0 and template[index - 1] == '#':
                        template[index] = {
                            'name': word,
                            'index': args.index(word),
                            'string': True
                        }
                        template.pop(index - 1)
                        continue
                    template[index] = {
                        'name': word,
                        'index': args.index(word),
                        'string': False
                    }
                index += 1
            if node_name in context.func_macro_map or node_name in context.object_macro_map:
                raise CompileNodeError('Duplicate preprocessor #define "%s"' % (node_name), node=type_node)
            context.func_macro_map[node_name] = {
                'arguments': args,
                'template': template,
                'node': type_node
            }
            return
        object_macro = re.fullmatch(r'\s*#\s*define\s+(\w+)\s+(.*)', code)
        if object_macro is not None:
            macro_name = object_macro.group(1)
            if macro_name != node_name:    
                raise CompileNodeError('Unable to parse <type category="define" name="%s"> node: #define directive is for different name %s' % (node_name, macro_name), node=type_node)
            code = object_macro.group(2)
            if node_name in context.func_macro_map or node_name in context.object_macro_map:
                raise CompileNodeError('Duplicate preprocessor #define "%s"' % (node_name))
            context.object_macro_map[node_name] = {
                'code': code,
                'node': type_node
            }
            return
        raise CompilerError('Unable to parse <type category="define" name="%s">: node is not empty, but does not contain function or object macro' % (node_name), node=type_node)
    
    def _enumerate_type_basetype_node(self, context: Context, type_node: Node):
        name = self.get_node_name(type_node)
        if name in context.ctypes_map:
            return
        words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in type_node.get_text_nodes_before(type_node.get('name'))]))]
        words = [x for x in words if x]
        if 'typedef' not in words:
            if words[-1] == 'struct':
                context.ctypes_map[name] = CType()
                return
            raise CompilerError('Basetype "%s" not a typedef or struct' % (name), node=type_node)
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
            raise CompilerError('Basetype "%s" is a typedef to an unknown type "%s"' % (name, ctype), node=type_node)
        while ptr_count > 0:
            ctype = ctype.pointer()
            ptr_count -= 1
        context.ctypes_map[name] = ctype
   
    def _enumerate_uncategorized_type(self, context: Context, type_node: Node):
        name = self.get_node_name(type_node)
        if name in context.ctypes_map:
            return
        if name in context.uncategorized_types:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.uncategorized_types[name])
        context.uncategorized_types[name] = type_node
    
    def _enumerate_type_bitmask_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_children(type_node)
        if name in context.bitmask_node_map:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.bitmask_node_map[name])
        context.bitmask_node_map[name] = type_node

    def _enumerate_type_handle_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_children(type_node)
        if name in context.handle_node_map:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.handle_node_map[name])
        context.handle_node_map[name] = type_node

    def _enumerate_type_enum_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_attribute(type_node)
        if name in context.enum_node_map:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.enum_node_map[name])
        context.enum_node_map[name] = type_node

    def _enumerate_type_struct_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_attribute(type_node)
        if name in context.complex_type_node_map:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.complex_type_node_map[name])
        context.complex_type_node_map[name] = type_node
    
    def _enumerate_type_union_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_attribute(type_node)
        if name in context.complex_type_node_map:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.complex_type_node_map[name])
        context.complex_type_node_map[name] = type_node

    def _enumerate_type_funcpointer_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_children(type_node)
        if name in context.callback_node_map:
            raise DuplicateNodeNameError(node=type_node, name=name, prev_node=context.callback_node_map[name])
        context.callback_node_map[name] = type_node

    def _enumerate_enum_nodes(self, context: Context, root_node: Node):
        for enums_node in root_node.get_all('enums'):
            if not context.is_target_api(enums_node):
                continue
            enums_name = self.get_node_name_from_attribute(enums_node)
            enums_type = enums_node.get_attribute('type')
            if enums_type in ['enum', 'bitmask']:
                is_in_enum = True
            elif enums_type is None:
                is_in_enum = False
            else:
                raise CompileNodeError('Node <enums name="%s"> unknown enum type "%s"' % (enums_name, enums_type), node=enums_node)
            if enums_name in context.enums_node_map:
                raise DuplicateNodeNameError(node=enums_node, name=enums_name, prev_node=context.enums_node_map[enums_name])
            context.enums_node_map[enums_name] = enums_node
            for enum_node in enums_node.get_all('enum'):
                if not context.is_target_api(enum_node):
                    continue
                enum_name = self.get_node_name_from_attribute(enum_node)
                if enum_node.has_attribute('alias'):
                    self._enumerate_alias_node(context, enum_node)
                    continue
                if enum_name in context.enum_value_map:
                    raise DuplicateNodeNameError(node=enum_node, name=enum_name, prev_node=self.enum_value_map[enum_name]['value_node'])
                context.enum_value_map[enum_name] = { 'value_node': enum_node }
                if enum_node.has_attribute('type'):
                    enum_type = enum_node.get_attribute('type')
                    if enum_type not in context.ctypes_map:
                        raise CompileNodeError('Enum node refers to unknown type "%s".', node=enum_node)
                    context.enum_value_map[enum_name]['type'] = context.ctypes_map[enum_type]
                if is_in_enum:
                    context.enum_value_map[enum_name]['enum_node'] = enums_node
                    context.enum_value_map[enum_name]['enum_name'] = enums_name
    
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
                if name in context.command_node_map:
                    raise DuplicateNodeNameError(node=command_node, name=name, prev_node=context.command_node_map[name])
                context.command_node_map[name] = command_node
    
    def _compile_handle_node_map(self, context: Context):
        for name, node in context.handle_node_map.items():
            if not context.is_target_api(node):
                continue
            typedef = node.get('type').get_text()
            # One of [VK_NULL_HANDLE, VK_DEFINE_NON_DISPATCHABLE_HANDLE]
            ctype = handle_type_map[typedef]
            if name in context.ctypes_map:
                raise CompileNodeError('Handle node type "%s" already defined as %r' % (name, context.ctypes_map[name]), node=node)
            context.ctypes_map[name] = ctype

    def _compile_enums(self, context: Context):
        name: str
        node: Node
        for name, node in context.bitmask_node_map.items():
            if not context.is_target_api(node):
                continue
            if 'type' not in node.children:
                raise CompileNodeError('Missing child <type> for node <type category="%s" name="%s">' % (node.get_attribute('category'), name), node=node)
            if len(node.children['type']) > 1:
                raise MultipleChildrenNodeError(node=node, name='type', count=len(node.children['type']))
            ctype_name = node.get('type').get_text()
            if ctype_name not in context.ctypes_map:
                raise CompileNodeError('Node <type category="%s" name="%s"> use unknown type "%s"' % (node.get_attribute('category'), name, ctype_name), node=node)
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
                if bit_name in context.bit_map:
                    raise CompileNodeError('In %s, name="%s": Bitmask assigns "%s" enum, already assigned by another bitmask "%s"' % (self.make_path(node), name, bit_name, self.bit_map[bit_name]))
                context.bit_map[bit_name] = name
        for name, node in context.enum_node_map.items():
            if name in context.bit_map:
                if context.bit_map[name] not in context.ctypes_map:
                    raise CompileNodeError('Expected "%s" for node <type category="enum"> to be known type' % (name), node=node)
                ctype = context.ctypes_map[context.bit_map[name]]
            else:
                ctype = ctypes_map['c_int']
            if name in context.ctypes_map:
                raise CompileNodeError('Enum "%s" already in ctypes' % (name), node=node)
            context.ctypes_map[name] = ctype
    
    def _get_enum_value(self, context: Context, node: Node):
        if node.has_attribute('bitpos'):
            bitpos = context.cparser.parse_c_int(node.get_attribute('bitpos'))
            return 1 << bitpos
        if node.has_attribute('value'):
            value = context.get_c_constant_value('int', node.get_attribute('value'))
            return value
        raise CompileNodeError('Missing enum value: Neither @value, nor @bitpos pressent', node=node)

    def _compile_enum_values(self, context: Context):
        for name, source_map in context.enum_value_map.items():
            value = self._get_enum_value(context, source_map['value_node'])
            if 'enum_node' not in source_map:
                node = source_map['value_node']
                ctype = node.get_attribute('type')
                if ctype is None:
                    raise CompileNodeError('Missing type for const node "%s"' % (name), node=node)
                if ctype not in basic_ctypes:
                    raise CompileNodeError('Invalid type "%s" for const node "%s", not in basic C types' % (ctype, name), node=node)
                ctype = basic_ctypes[ctype]
                value = ctype.make_python_value(value)
            else:
                assert 'enum_name' in source_map, "'enum_name' in source_map"
                assert source_map['enum_name'] in context.ctypes_map, "source_map['enum_name'] in context.ctypes_map"
                context.ctypes_map[source_map['enum_name']].make_python_value(value)
                context.value_enum_map[name] = source_map['enum_name']
            source_map['value'] = value
            if name in context.value_map:
                raise CompilerError('Value "%s" already defined' % (name))
            context.value_map[name] = value
    
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

    def _compile_feature_enum_values(self, context: Context):
        root_node: Node
        for root_node in self.xml_map.values():
            for feature_node in root_node.get_all('feature'):
                if not context.is_target_api(feature_node):
                    continue
                feature_name = self.get_node_name_from_attribute(feature_node)
                for require_node in feature_node.get_all('require'):
                    if not context.is_target_api(require_node):
                        continue
                    for enum_node in require_node.get_all('enum'):
                        if not context.is_target_api(enum_node):
                            continue
                        if enum_node.has_attribute('alias'):
                            self._enumerate_alias_node(context, enum_node)
                            continue
                        enum_name = self.get_node_name_from_attribute(enum_node)
                        extend_name = None
                        if enum_node.has_attribute('extends'):
                            extend_name = enum_node.get_attribute('extends')
                            if extend_name not in context.enum_node_map:
                                raise CompileNodeError('Feature "%s", enum "%s": Extending non-existent enum "%s"' % (feature_name, enum_name, extend_name), node=enum_node)
                        value = self._get_feature_enum_value(context, enum_node, feature_node)
                        if value is None:
                            continue
                        if enum_name in context.value_map:
                            if context.value_map[enum_name] != value:
                                raise CompileNodeError('Feature "%s", enum "%s" = (%r) is already defined in value map with different value (%r)' % (feature_name, enum_name, value, context.value_map[enum_name]))
                            if extend_name is not None and not enum_node.has_attribute('extnumber'):
                                assert enum_name in self.enum_value_map, 'enum_name in self.enum_value_map'
                                context.enum_value_map[enum_name]['value_node'] = enum_node
                                context.enum_value_map[enum_name]['feature_node'] = feature_node
                        else:
                            assert enum_name not in context.enum_value_map, 'enum_name not in context.enum_value_map'
                            assert enum_name not in context.value_enum_map, 'enum_name not in context.value_enum_map'
                            context.value_map[enum_name] = value
                            context.enum_value_map[enum_name] = {
                                'value_node': enum_node,
                                'feature_node': feature_node
                            }
                            if extend_name is not None:
                                context.enum_value_map[enum_name]['enum_name'] = extend_name
                                context.enum_value_map[enum_name]['enum_node'] = context.enum_node_map[extend_name]
                                context.value_enum_map[enum_name] = extend_name
    
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

    def _compile_ext_enum_values(self, context: Context):
        root_node: Node
        for root_node in self.xml_map.values():
            for extensions_node in root_node.get_all('extensions'):
                if not context.is_target_api(extensions_node):
                    continue
                for ext_node in extensions_node.get_all('extension'):
                    if not context.is_target_api(ext_node):
                        continue
                    ext_name = self.get_node_name_from_attribute(ext_node)
                    for require_node in ext_node.get_all('require'):
                        if not context.is_target_api(require_node):
                            continue
                        for enum_node in require_node.get_all('enum'):
                            if not context.is_target_api(enum_node):
                                continue
                            if enum_node.has_attribute('alias'):
                                self._enumerate_alias_node(context, enum_node)
                                continue
                            enum_name = self.get_node_name_from_attribute(enum_node)
                            extend_name = None
                            if enum_node.has_attribute('extends'):
                                extend_name = enum_node.get_attribute('extends')
                                if extend_name not in context.enum_node_map:
                                    raise CompileNodeError('In extension "%s", enum "%s": Extending non-existent enum "%s"' % (ext_name, enum_name, extend_name), node=enum_node)
                            value = self._get_ext_enum_value(context, enum_node, ext_node)
                            if value is None:
                                continue
                            if enum_name in context.value_map:
                                if context.value_map[enum_name] != value:
                                    raise CompileNodeError('In extension "%s", enum "%s" = (%r) is already defined in value map with different value (%r)' % (ext_name, enum_name, value, context.value_map[enum_name]), node=enum_node)
                                if extend_name is not None and not enum_node.has_attribute('extnumber'):
                                    assert enum_name in context.enum_value_map, 'enum_name in self.enum_value_map'
                                    context.enum_value_map[enum_name]['value_node'] = enum_node
                                    context.enum_value_map[enum_name]['ext_node'] = ext_node
                            else:
                                assert enum_name not in context.enum_value_map, 'enum_name not in self.enum_value_map'
                                assert enum_name not in context.value_enum_map, 'enum_name not in self.value_enum_map'
                                context.value_map[enum_name] = value
                                context.enum_value_map[enum_name] = {
                                    'value_node': enum_node,
                                    'ext_node': ext_node
                                }
                                if extend_name is not None:
                                    context.enum_value_map[enum_name]['enum_name'] = extend_name
                                    context.enum_value_map[enum_name]['enum_node'] = context.enum_node_map[extend_name]
                                    context.value_enum_map[enum_name] = extend_name

    def _compile_callback_node_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.callback_node_map.items():
            if not name.startswith('PFN_'):
                raise CompileNodeError('Expected callback name to be function pointer named starting with PFN_', node=node)
            fn_type = context.ctypes_map[name[4:]] = CFunctionType(name[4:])
            fn_type['node'] = node
            fn_type['name'] = name
            context.ctypes_map[name] = fn_type.pointer()

    def _compile_uncategorized_types(self, context: Context):
        # While it is an error to use uncategorized type, it is not an error to use a pointer to uncategorized type.
        # Pointer to uncategorized types are pointer to black-box structures, thus handled as void*.
        for name in context.uncategorized_types:
            if name not in context.ctypes_map and name not in context.complex_type_node_map:
                context.ctypes_map[name] = CType()
    
    def _compile_complex_types(self, context: Context):
        for name, node in context.complex_type_node_map.items():
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
                enum_value = context.value_map[enum_name]
                if isinstance(enum_value, str):
                    enum_value = context.cparser.generate_c_string(enum_value)
                else:
                    assert isinstance(enum_value, int) or isinstance(enum_value, float), 'isinstance(enum_value, int) or isinstance(enum_value, float)'
                    enum_value = str(enum_value)
                code.append(enum_value)
                continue
            code.append(child.get_text())
        return ''.join(code)
    
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
            for member_node in node.get_all('member'):
                if not context.is_target_api(member_node):
                    continue
                member_name = self.get_node_name_from_children(member_node)
                ctype.member_map[member_name] = {'node': member_node}
                ctype.member_list.append(member_name)
                if 'type' not in member_node.children:
                    raise CompileNodeError('Member "%s.%s": Missing attribute @type' % (name, member_name), node=member_node)
                if len(member_node.children['type']) > 1:
                    raise MultipleChildrenNodeError(node=member_node, name='type', count=len(member_node.children['type']))
                member_type = member_node.get('type').get_text()
                while member_type in context.alias_map:
                    member_type = context.alias_map[member_type]
                if member_type in context.resolving_complex_type:
                    assert member_type in context.ctypes_map, 'member_type in context.ctypes_map'
                    assert member_type in context.complex_type_node_map, 'member_type in context.complex_type_node_map'
                    assert isinstance(context.ctypes_map[member_type], CComplexType), 'isinstance(context.ctypes_map[member_type], CComplexType)'
                    ctype['delay_fields'] = True
                    ctype['dependencies'].append(member_type)
                elif member_type not in context.ctypes_map:
                    if member_type in context.complex_type_node_map:
                        self._compile_complex_type(context, member_type, context.complex_type_node_map[member_type])
                        assert member_type in context.ctypes_map, 'member_type in context.ctypes_map'
                    else:
                        # Foreign types must have been resolved at this time (see category="basetype")
                        raise CompileNodeError('Member "%s.%s": Reference to unknow type "%s"' % (name, member_name, member_type))
            self._resolve_complex_type(context, name, node)
        finally:
            context.resolving_complex_type.remove(name)
    
    def _resolve_callback_type_map(self, context: Context):
        name: str
        node: Node
        for name, node in context.callback_node_map.items():
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
            assert context.ctypes_map[name[4:]].pointer() is context.ctypes_map[name]
            fn_decl = ast.ext[0].type.type
            ctype = context.ctypes_map[name[4:]]
            assert isinstance(ctype, CFunctionType), 'isinstance(ctype, CFunctionType)'
            ctype.constructor = 'VKAPI_PTR'
            for param in fn_decl.args.params:
                param_ctype = context.get_type_from_decl(param.type)
                ctype.argument_types.append(param_ctype)
                if param.name == 'pUserData':
                    ctype['user_data'] = len(ctype.argument_types) - 1
            return_ctype = context.get_type_from_decl(fn_decl.type)
            ctype.return_type = return_ctype

    def _compile_commands(self, context: Context):
        name: str
        node: Node
        for name, node in context.command_node_map.items():
            code = '%s(%s);' % (self._get_member_code(context, node.get('proto')), ', '. join([self._get_member_code(context, x) for x in node.get_all('param')]))
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
            if name in context.ctypes_map:
                raise CompileNodeError('Command "%s" already is context.ctypes' % (name), node=node)
            context.ctypes_map[name] = ctype
    
    def _resolve_enums(self, context: Context):
        for name, value in context.value_enum_map.items():
            if value not in context.value_type_map:
                context.value_type_map[value] = {}
            value_type_map = context.value_type_map[value]
            assert name not in value_type_map, 'name not in value_type_map'
            value_type_map[name] = context.value_map[name]
        enums_name: str
        enums_node: Node
        for enums_name, enums_node in context.enums_node_map.items():
            if enums_node.has_attribute('type'):
                enum_type = enums_node.get_attribute('type')
            else:
                enum_type = None
            if enum_type == 'enum':
                if enums_name in context.value_type_map:
                    value_map = context.enum_type_map[enums_name] = context.value_type_map[enums_name]
            elif enum_type == 'bitmask':
                if enums_name in context.value_type_map:
                    value_map = context.bitmask_type_map[enums_name] = context.value_type_map[enums_name]
                if enums_name not in context.bit_map:
                    maybe_type_name = enums_name.replace('Bits', '').replace('Flag', 'Flags')
                    if maybe_type_name in context.bitmask_node_map:
                        context.bit_map[enums_name] = maybe_type_name
            else:
                for enum_node in enums_node.get_all('enum'):
                    enum_name = enum_node.get_attribute('name')
                    if enum_node.has_attribute('alias'):
                        if enum_node.get_attribute('deprecated') != 'aliased':
                            context.const_map[enum_name] = {
                                'value': context.cgenerator.Code(enum_node.get_attribute('alias')),
                                'alias': enum_node.get_attribute('alias'),
                                'node': enum_node
                            }
                    else:
                        assert enum_node.has_attribute('type'), "enum_node.has_attribute('type')"
                        ctype = context.ctypes_map[enum_node.get_attribute('type')]
                        context.const_map[enum_name] = {
                            'value': context.value_map[enum_name],
                            'ctype': ctype,
                            'node': enum_node
                        }
                continue
            for enum_node in enums_node.get_all('enum'):
                if enum_node.has_attribute('alias') and enum_node.get_attribute('deprecated') != 'aliased':
                    enum_name = enum_node.get_attribute('name')
                    enum_alias = enum_node.get_attribute('alias')
                    value_map[enum_name] = context.cgenerator.Code(enum_alias)

    def compile(self, context = Context()):
        for root_node in self.xml_map.values():
            self._enumerate_type_nodes(context, root_node)
            self._enumerate_enum_nodes(context, root_node)
            self._enumerate_command_nodes(context, root_node)
        self._compile_handle_node_map(context)
        self._compile_enums(context)
        self._compile_enum_values(context)
        self._compile_feature_enum_values(context)
        self._compile_ext_enum_values(context)
        self._compile_callback_node_map(context)
        self._compile_uncategorized_types(context)
        self._compile_complex_types(context)
        self._resolve_callback_type_map(context)
        self._compile_commands(context)
        self._resolve_enums(context)

        return context