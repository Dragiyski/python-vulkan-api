import pycparser
import pycparser.c_ast
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, CType, CArrayType
from .xml_parser import Node

class Context:
    def __init__(self, api='vulkan'):
        self.ctypes_map = {**basic_ctypes, **platform_ctypes}
        self.object_macro_map = dict(object_macro_map)
        self.func_macro_map = dict(func_macro_map)
        self.alias_map = {}
        self.value_map = {}
        self.define_node_map = {}
        self.value_enum_map = {}
        self.alias_node_map = {}
        self.enum_node_map = {}
        self.enums_node_map = {}
        self.value_node_map = {}
        self.enum_type_map = {}
        self.bitmask_type_map = {}
        self.value_type_map = {}
        self.bitmask_node_map = {}
        self.handle_node_map = {}
        self.uncategorized_types = {}
        self.complex_type_node_map = {}
        self.callback_node_map = {}
        self.command_node_map = {}
        self.enum_value_map = {}
        self.const_map = {}
        self.bit_map = {}
        self.api = api

        from .cparser import CParser, CGenerator
        self.cparser = CParser(self)
        self.cgenerator = CGenerator()
        self.resolving_complex_type = set()

    def is_target_api(self, node: Node):
        if not node.has_attribute('api'):
            return True
        api = node.get_attribute('api')
        api = [str.strip(x).lower() for x in api.split(',')]
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
            return self.value_map[node.name]
        elif node_type is c_ast.Cast:
            target_type = self.get_type_from_decl(node.to_type.type)
            value = self.get_c_ast_const_value(node.expr)
            return target_type.make_python_value(value)
        
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
