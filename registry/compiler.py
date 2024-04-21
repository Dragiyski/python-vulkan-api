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
        if name in context.alias_node_map:
            if context.alias_node_map[name] != node:
                raise DuplicateNodeNameError(node=node, name=name, prev_node=context.alias_node_map[name])
        context.alias_node_map[name] = node
        context.alias_map[alias] = name

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
            value = self.get_enum_value(enum_node)
        else:
            return None
        if enum_node.get_attribute('dir') == '-':
            value = -value
        return value

    def _compile_feature_enum_values(self, context: Context):
        root_node: Node
        for root_node in self.xml_map.values():
            for feature_node in root_node.get_all('feature'):
                feature_name = self.get_node_name_from_attribute(feature_node)
                for require_node in feature_node.get_all('require'):
                    for enum_node in require_node.get_all('enum'):
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
                                self.enum_value_map[enum_name]['value_node'] = enum_node
                                self.enum_value_map[enum_name]['feature_node'] = feature_node
                                if 'ext_node' in self.enum_value_map[enum_name]:
                                    del self.enum_value_map[enum_name]['ext_node']
                        else:
                            assert enum_name not in self.enum_value_map, 'enum_name not in self.enum_value_map'
                            assert enum_name not in self.value_enum_map, 'enum_name not in self.value_enum_map'
                            self.value_map[enum_name] = value
                            self.enum_value_map[enum_name] = {
                                'value_node': enum_node,
                                'feature_node': feature_node
                            }
                            if extend_name is not None:
                                self.enum_value_map[enum_name]['enum_name'] = extend_name
                                self.enum_value_map[enum_name]['enum_node'] = self.enum_node_map[extend_name]
                                self.value_enum_map[enum_name] = extend_name

    def compile(self, context = Context()):
        for root_node in self.xml_map.values():
            self._enumerate_type_nodes(context, root_node)
            self._enumerate_enum_nodes(context, root_node)
            self._enumerate_command_nodes(context, root_node)
        self._compile_handle_node_map(context)
        self._compile_enums(context)
        self._compile_enum_values(context)

        cparser = CParser(context)
        cgenerator = CGenerator(reduce_parentheses=True)

        return context