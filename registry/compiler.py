import re
import os
from collections import OrderedDict
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines, PythonCode
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CPointerType, CComplexType, CArrayType, CFunctionType

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

def make_path(self, node):
    names = []
    while node is not None:
        exposed_attr = []
        if node.has_attribute('category'):
            exposed_attr.append('category="%s"' % node.get_attribute('category'))
        if node.has_attribute('name'):
            exposed_attr.append('name="%s"' % node.get_attribute('name'))
        if node.has_attribute('alias'):
            exposed_attr.append('alias="%s"' % node.get_attribute('alias'))
        names.append('<%s>' % node.node_name)
        node = node.parent_node
    return '/'.join(names)

class Compiler:
    class Context:
        def __init__(self, api='vulkan'):
            self.ctypes_map = {**basic_ctypes, **platform_ctypes}
            self.object_macro_map = dict(object_macro_map)
            self.func_macro_map = dict(func_macro_map)
            self.alias_map = {}
            self.value_map = {}
            self.value_enum_map = {}
            self.enum_node_map = {}
            self.enums_node_map = {}
            self.value_node_map = {}
            self.bitmask_node_map = {}
            self.handle_node_map = {}
            self.uncategorized_types = {}
            self.complex_type_node_map = {}
            self.callback_node_map = {}
            self.command_node_map = {}
            self.enum_value_map = {}
            self.const_map = {}
            self.bit_map = {}
            self.resolving_complex_type = set()
            self.api = api

            class CParser(pycparser.CParser):
                def _lex_type_lookup_func(parser, name):
                    if super()._lex_type_lookup_func(name):
                        return True
                    while name in self.alias_map:
                        name = self.alias_map[name]
                    return name in self.ctypes_map
            
            self.cparser = CParser()
            self.cgenerator = CGenerator()

        def is_target_api(self, node):
            if not node.has_attribute('api'):
                return True
            api = node.get_attribute('api')
            api = [str.strip(x).lower() for x in api.split(',')]
            return self.api in api

    def __init__(self):
        self.xml_map = OrderedDict()

    def add_xml_file(self, file):
        if (file in self.xml_map):
            raise ValueError('Adding already processed file: %s' % (file))
        root_node = parse_xml(file)
        self.xml_map[file] = root_node

    # TODO: Check https://github.com/paulross/cpip for full-blown C/C++ preprocessor in python
    def _process_type_nodes(self, context, root_node):
        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                if not context.is_target_api(type_node):
                    continue
                if type_node.has_attribute('alias'):
                    self._process_alias_node(context, type_node)
                else:
                    category = type_node.get_attribute('category')
                    if category == 'define':
                        self._process_type_define_node(context, type_node)
                    elif category == 'basetype':
                        self._process_type_basetype_node(context, type_node)
                    elif category is None:
                        self._process_uncategorized_type(context, type_node)
                    elif category == 'bitmask':
                        self._process_type_bitmask_node(context, type_node)
                    elif category == 'handle':
                        self._process_type_handle_node(context, type_node)
                    elif category == 'enum':
                        self._process_type_enum_node(context, type_node)
                    elif category == 'struct':
                        self._process_type_struct_node(context, type_node)
                    elif category == 'union':
                        self._process_type_union_node(context, type_node)
                    elif category == 'funcpointer':
                        self._process_type_funcpointer_node(context, type_node)

    @staticmethod
    def multiple_children_error(node, child_name):
        child_count = len(node.children[child_name])
        return CompilerError('Expected a single child <%s>, but found %d children' % (child_name, child_count), node=node)

    @staticmethod
    def get_node_name(node):
        if node.has_attribute('name'):
            return node.get_attribute('name')
        if 'name' in node.children:
            if len(node.children['name']) > 1:
                raise Compiler.multiple_children_error(node, 'name')
            return node.get('name').get_text()
        raise CompilerError('Missing node name: expected either attribute @name or child element <name>', node=node)
    
    @staticmethod
    def get_node_name_from_children(node):
        if 'name' not in node.children:
            raise CompilerError('Missing node name: expected child element <name>', node=node)
        if len(node.children['name']) > 1:
            raise Compiler.multiple_children_error(node, 'name')
        return node.get('name').get_text()
    
    @staticmethod
    def get_node_name_from_attribute(node):
        if not node.has_attribute('name'):
            raise CompilerError('Missing node name: expected attribute @name', node=node)
        return node.get_attribute('name')
    
    def _process_alias_node(self, context: Context, node: Node):
        assert node.has_attribute('alias'), "node.has_attribute('alias')"
        name = self.get_node_name_from_attribute(node)
        alias = node.get_attribute('alias')
        if name in context.alias_map:
            if context.alias_map[name] != alias:
                raise CompilerError('Duplicate alias "%s": The referred alias "%s" does not match previously defined value "%s"' % (name, alias, context.alias_map[name]), node=node)

    def _process_type_define_node(self, context: Context, type_node: Node):
        node_name = self.get_node_name(type_node)
        code = type_node.get_text()
        code = get_preprocessor_lines(code)
        if len(code) > 1:
            raise CompilerError('Unable to parse <type category="define" name="%s"> node: expected single #define directive' % (node_name), node=type_node)
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
                raise CompilerError('Duplicate preprocessor #define "%s"' % (node_name), node=type_node)
            self.func_macro_map[node_name] = {
                'arguments': args,
                'template': template,
                'node': type_node
            }
            return
        object_macro = re.fullmatch(r'\s*#\s*define\s+(\w+)\s+(.*)', code)
        if object_macro is not None:
            macro_name = object_macro.group(1)
            if macro_name != node_name:    
                raise CompilerError('Unable to parse <type category="define" name="%s"> node: #define directive is for different name %s' % (node_name, macro_name), node=type_node)
            code = object_macro.group(2)
            if node_name in self.func_macro_map or node_name in self.object_macro_map:
                raise CompilerError('Duplicate preprocessor #define "%s"' % (node_name))
            self.object_macro_map[node_name] = {
                'code': code,
                'node': type_node
            }
            return
        raise CompilerError('Unable to parse <type category="define" name="%s">: node is not empty, but does not contain function or object macro' % (node_name), node=type_node)
    
    def _process_type_basetype_node(self, context: Context, type_node: Node):
        name = self.get_node_name(type_node)
        if name in context.ctypes_map:
            return
        words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in type_node.get_text_nodes_before(type_node.get('name'))]))]
        words = [x for x in words if x]
        if 'typedef' not in words:
            if words[-1] == 'struct':
                self.ctypes_map[name] = CType()
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
        elif ctype in self.ctypes_map:
            ctype = self.ctypes_map[ctype]
        else:
            raise CompilerError('Basetype "%s" is a typedef to an unknown type "%s"' % (name, ctype), node=type_node)
        while ptr_count > 0:
            ctype = ctype.pointer()
            ptr_count -= 1
        context.ctypes_map[name] = ctype

    def _process_type_node_save_in_map(self, context: Context, node: Node, category, map_name: str, name: str):
        if name in getattr(context, map_name):
            raise CompilerError('Duplicate %sname="%s">' % ((('category="%s" ' % str(category)) if category is not None else ''), name))
        getattr(context, map_name)[name] = node
    
    def _process_uncategorized_type(self, context: Context, type_node: Node):
        name = self.get_node_name_from_attribute(type_node)
        self._process_type_node_save_in_map(context, type_node, None, 'uncategorized_types', name)
    
    def _process_type_bitmask_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_children(type_node)
        if name in context.bitmask_node_map:
            raise CompilerError('Duplicate <type category="bitmask" name="%s">', node=type_node)
        context.bitmask_node_map[name] = type_node

    def _process_type_handle_node(self, context: Context, type_node: Node):
        name = self.get_node_name_from_children(type_node)
        if name in context.handle_node_map:
            raise CompilerError('Duplicate <type category="handle" name="%s">', node=type_node)
        context.handle_node_map[name] = type_node


    def run(context = Context()):
        pass