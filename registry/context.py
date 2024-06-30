import ast
import re
import pycparser
import pycparser.c_ast
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, CType, CArrayType, CPlainType
from .xml_parser import Node
from ast import parse as parse_python, unparse as unparse_python

class NameMap(dict):
    class DuplicateKeyError(Exception):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            self.__dict__.update(**kwargs)

    def set(self, name, value):
        if name in self:
            raise self.DuplicateKeyError('Name "%s" already exists' % name, name=name, old_value=self[name], new_value=value)
        self[name] = value

class NameListMap(dict):
    def set(self, name, value):
        if name not in self:
            self[name] = []
        self[name].append(value)

class Alias(str):
    def __new__(cls, value):
        self = str.__new__(cls, str(value))
        self.data = {}
        self.node_set = set()
        return self

class Context:
    def __init__(self, api='vulkan'):
        self.tag_set = set()
        self.type_node_map = {
            'define': NameMap(),
            'basetype': NameMap(),
            'unknown': NameMap(),
            'bitmask': NameMap(),
            'handle': NameMap(),
            'enum': NameMap(),
            'set': NameMap(),
            'struct': NameMap(),
            'union': NameMap(),
            'complex': NameMap(),
            'funcpointer': NameMap(),
            'all': NameMap()
        }
        self.enums_node_map = NameMap()
        self.enum_node_map = NameMap()
        self.command_node_map = NameMap()
        self.ctypes_map = {**basic_ctypes, **platform_ctypes}
        self.object_macro_map = dict(object_macro_map)
        self.func_macro_map = dict(func_macro_map)
        self.alias_map = {}
        self.handle_map = NameMap()
        # All constants must go into the value map *only*
        # If they belong to enum, it must have 'enum' key, containing the enum name.
        # If the value has been added by a feature or an extension, it must have have 'feature' or 'extension' key as a list of dict.
        # The value must have associated ctype:
        # If part of enum/bitmask, it must have the same type as the enum/bitmask if omitted.
        # If not part of enum, the type is reqired.
        self.value_map = NameMap()
        # self.enum_value_map = {}
        # self.const_map = {}
        # Contains a map of all enums, enum has a required ctype (defaults to "int" if not specified).
        self.enum_map = NameMap()
        # Maps bitmask name to enum name.
        self.bit_map = NameMap()
        self.struct_map = NameMap()
        # Map commands
        self.command_name_map = NameMap()
        self.command_map = NameMap()
        self.callback_map = NameMap()
        self.api = api
        # self.base_vulkan_types = {}
        # self.enum_base_type = {}
        # self.bitmask_base_type = {}
        # self.value_base_type = {}
        self.feature_map = NameMap()
        self.ext_map = NameMap()

        from .cparser import CParser, CGenerator
        self.cparser = CParser(self)
        self.cgenerator = CGenerator()
        self.resolving_complex_type = set()

        self.plain_ctype_class = {
            'enum': {},
            'bitmask': {},
            'value': {}
        }

    def is_target_api(self, node: Node):
        if not node.has_attribute('api'):
            return True
        api = node.get_attribute('api')
        return self.is_target_api_value(api)
    
    def is_target_api_value(self, value: str):
        api = [str.strip(x).lower() for x in value.split(',')]
        return self.api in api
    
    def preprocess_c_code(self, code: str):
        ast = self.cparser.parse(code)
        while self.preprocess_c_ast(ast):
            code = self.cgenerator.visit(ast)
            ast = self.cparser.parse(code)
        return code
    
    def preprocess_c_ast(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.object_macro_map:
                setattr(node, name, self.cgenerator.Code(self.object_macro_map[child_node.name]['code']))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.func_macro_map:
                args = [self.cgenerator.visit(x) for x in child_node.args]
                macro = self.func_macro_map[child_node.name.name]
                if len(macro['arguments']) != len(args):
                    raise self.cparser.ParseError('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro['arguments'], len(args))))
                code = []
                for part in macro['template']:
                    if isinstance(part, str):
                        code.append(part)
                    else:
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, self.cgenerator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.preprocess_c_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution
    
    def get_c_constant_value(self, ctype: str, value):
        from .cparser import CParser
        if ctype not in self.ctypes_map:
            raise CParser.ParseError('Unknown ctype: %s' % (ctype))
        code = '%s value = %s;' % (ctype, value)
        code = self.preprocess_c_code(code)
        ast = self.cparser.parse(code)
        return self.get_c_ast_const_value(ast.ext[0].init)
    
    def get_c_ast_const_value(self, node: pycparser.c_ast.Node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return self.cparser.parse_c_int(node.value)
            if node.type in ['float', 'double']:
                return self.cparser.parse_c_float(node.value)
            if node.type == 'string':
                return self.cparser.parse_c_string(node.value)
        elif node_type is c_ast.UnaryOp:
            if node.op == '~':
                return ~self.get_c_ast_const_value(node.expr)
            if node.op == '+':
                return +self.get_c_ast_const_value(node.expr)
            if node.op == '-':
                return -self.get_c_ast_const_value(node.expr)
        elif node_type is c_ast.BinaryOp:
            if node.op == '|':
                return self.get_c_ast_const_value(node.left) | self.get_c_ast_const_value(node.right)
            if node.op == '&':
                return self.get_c_ast_const_value(node.left) & self.get_c_ast_const_value(node.right)
            if node.op == '^':
                return self.get_c_ast_const_value(node.left) ^ self.get_c_ast_const_value(node.right)
            if node.op == '+':
                return self.get_c_ast_const_value(node.left) + self.get_c_ast_const_value(node.right)
            if node.op == '-':
                return self.get_c_ast_const_value(node.left) - self.get_c_ast_const_value(node.right)
            if node.op == '*':
                return self.get_c_ast_const_value(node.left) * self.get_c_ast_const_value(node.right)
            if node.op == '/':
                return self.get_c_ast_const_value(node.left) / self.get_c_ast_const_value(node.right)
            if node.op == '%':
                return self.get_c_ast_const_value(node.left) % self.get_c_ast_const_value(node.right)
            if node.op == '<<':
                return self.get_c_ast_const_value(node.left) << self.get_c_ast_const_value(node.right)
            if node.op == '>>':
                return self.get_c_ast_const_value(node.left) >> self.get_c_ast_const_value(node.right)
        elif node_type is c_ast.ID:
            if node.name not in self.value_map:
                raise self.cparser.ParseError('Missing ID: %s' % node.name)
            return self.value_map[node.name]['value']
        elif node_type is c_ast.Cast:
            target_type = self.get_type_from_decl(node.to_type.type)
            value = self.get_c_ast_const_value(node.expr)
            return target_type.make_python_value(value)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)
        
    def get_python_code_for_func_macro(self, name):
        if name not in self.func_macro_map:
            raise KeyError('No function macro named "%s" exists.' % name)
        descriptor = self.func_macro_map[name]
        from pycparser.c_parser import ParseError
        try:
            code = self.preprocess_c_code('int value = %s(%s);' % (name, ', '.join(descriptor['arguments'])))
        except ParseError:
            return None
        code_ast = self.cparser.parse(code)
        c_ast = pycparser.c_ast
        assert type(code_ast) is c_ast.FileAST
        assert type(code_ast.ext[0]) is c_ast.Decl
        assert isinstance(code_ast.ext[0].init, c_ast.Node)
        try:
            node = self.generate_python_ast_from_c_ast(code_ast.ext[0].init, descriptor['arguments'])
        except NotImplementedError:
            return None
        return_node = ast.Return(node)
        def_node = ast.FunctionDef(
            name=name,
            args=ast.arguments(
                args=[ast.arg(arg_name) for arg_name in descriptor['arguments']],
                posonlyargs=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]
            ),
            body=[return_node],
            decorator_list=[],
            lineno=0,
            col_offset=0
        )
        return def_node

    def generate_python_ast_from_c_ast(self, node: pycparser.c_ast.Node, args: list):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return ast.Constant(self.cparser.parse_c_int(node.value))
            elif node.type in ['float', 'double']:
                return ast.Constant(self.cparser.parse_c_float(node.value))
            elif node.type == 'string':
                return ast.Constant(self.cparser.parse_c_string(node.value))
        elif node_type is c_ast.UnaryOp:
            if node.op == '~':
                return ast.UnaryOp(op=ast.Invert(), operand=self.generate_python_ast_from_c_ast(node.expr, args))
            elif node.op == '+':
                return ast.UnaryOp(op=ast.UAdd(), operand=self.generate_python_ast_from_c_ast(node.expr, args))
            elif node.op == '-':
                return ast.UnaryOp(op=ast.USub(), operand=self.generate_python_ast_from_c_ast(node.expr, args))
        elif node_type is c_ast.BinaryOp:
            if node.op == '|':
                return ast.BinOp(op=ast.BitOr(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '&':
                return ast.BinOp(op=ast.BitAnd(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '^':
                return ast.BinOp(op=ast.BitXor(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '+':
                return ast.BinOp(op=ast.Add(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '-':
                return ast.BinOp(op=ast.Sub(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '*':
                return ast.BinOp(op=ast.Mult(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '/':
                return ast.BinOp(op=ast.Div(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '%':
                return ast.BinOp(op=ast.Mod(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '<<':
                return ast.BinOp(op=ast.LShift(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
            elif node.op == '>>':
                return ast.BinOp(op=ast.RShift(), left=self.generate_python_ast_from_c_ast(node.left, args), right=self.generate_python_ast_from_c_ast(node.right, args))
        elif node_type is c_ast.ID:
            if node.name not in args:
                raise self.cparser.ParseError('Missing ID: %s' % node.name)
            return ast.Name(node.name)
        elif node_type is c_ast.Cast:
            target_type = self.get_type_from_decl(node.to_type.type)
            if not isinstance(target_type, CPlainType):
                raise NotImplementedError('Casting to non-plain types is not supported: %r' % target_type)
            value_node = self.generate_python_ast_from_c_ast(node.expr, args)
            expr_node = ast.Attribute(
                value=ast.Call(
                    func=ast.Attribute(
                        value=ast.Name(id='ctypes'),
                        attr=target_type.parent_ctype,
                        ctx=ast.Load(lineno=0, col_offset=0)
                    ),
                    args=[
                        value_node
                    ],
                    keywords=[]
                ),
                attr='value',
                ctx=ast.Load(lineno=0, col_offset=0)
            )
            return expr_node
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)
        
    def get_type_from_decl(self, node) -> CType:
        if type(node) is pycparser.c_ast.PtrDecl:
            return self.get_type_from_decl(node.type).pointer()
        if type(node) is pycparser.c_ast.ArrayDecl:
            length = self.get_c_ast_const_value(node.dim)
            return CArrayType(self.get_type_from_decl(node.type), length)
        if type(node) is pycparser.c_ast.TypeDecl:
            if type(node.type) is pycparser.c_ast.IdentifierType:
                type_name = ' '.join(node.type.names)
            elif type(node.type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union]:
                type_name = node.type.name
            else:
                raise NotImplementedError('TODO: C: TypeDecl => %s' % type(node.type).__name__)
            while type_name in self.alias_map:
                type_name = self.alias_map[type_name]
            if type_name not in self.ctypes_map:
                raise self.cparser.ParseError('Reference to undefined type "%s"' % (type_name))
            return self.ctypes_map[type_name]
        raise NotImplementedError('TODO: C: %s' % type(node).__name__)

    def resolve_alias(self, name):
        while name in self.alias_map:
            name = self.alias_map[name]
        return name

    @staticmethod
    def make_python_name(name):
        words = name.split('_')
        words = [re.findall(r'(?:[A-Z][A-Z0-9]*|^)[a-z0-9]*', word) for word in words]
        words = [word.lower() for x in words for word in x]
        return words
