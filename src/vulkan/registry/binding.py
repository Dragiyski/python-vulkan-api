import ast
from types import MappingProxyType
import pycparser.c_ast
from ._nodes import nodes, bit_enum_map, category_name_map
from .platform import macro_ignore, platform_types, native_types
from .xml_parser import Node

_export_names = set(nodes.keys()).difference(bit_enum_map.keys()).difference(macro_ignore)

class Binding:
    def __init__(self):
        from ._c import CContext
        self.c_context = CContext()
        self.c_context.c_type.update(category_name_map['type'])
        self.c_context.c_type.update(category_name_map['struct'])
        self.c_context.c_type.update(category_name_map['union'])
        self.c_context.c_type.update(category_name_map['handle'])
        self.c_context.c_type.update(category_name_map['enum'])
        self.c_context.c_type.update(category_name_map['bitmask'])
        self.c_context.c_type.update({ k for k in category_name_map['alias'] for n in nodes[k] if n.has_attribute('alias') and n.get_attribute('alias') in self.c_context.c_type })
        self.vulkan_names = set()
        self.vulkan_values = {}
        self.vulkan_macros = {}
        for name in category_name_map['define']:
            if name in macro_ignore:
                continue
            node_set = nodes[name]
            for node in node_set:
                if node.get_path()[-2:] != ['types', 'type']:
                    continue
                try:
                    self.c_context.define(node.get_text())
                except self.c_context.DefinitionError:
                    pass
        for name in self.c_context.pp_value_code:
            try:
                self.vulkan_values[name] = self.c_context.get_constant_value(name)
            except NotImplementedError:
                pass
        macro_ast_def = {}
        for name in self.c_context.pp_func_code:
            try:
                macro_ast_def[name] = self.c_context.get_python_code_for_func_macro(name)
            except NotImplementedError:
                pass
        macro_ast_module = ast.Module(list(macro_ast_def.values()))
        ast.fix_missing_locations(macro_ast_module)
        vulkan_macros = {}
        exec(compile(macro_ast_module, '<vulkan.registry.macro>', 'exec'), vulkan_macros)
        for name in macro_ast_def.keys():
            self.vulkan_macros[name] = vulkan_macros[name]
        pass


    def __dir__(self):
        return object.__dir__(self) + list(_export_names)
    
    def __getattr__(self, name: str):
        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError(name)

    def __getitem__(self, name: str):
        try:
            value = self._get_binding(name)
        except NotImplementedError:
            raise KeyError(name)
        self.__dict__[name] = value
        return value
    
    def _get_binding(self, name):
        if name not in self.vulkan_names:
            raise KeyError(name)
        node = nodes[name]
        node: Node
        if name in category_name_map['alias']:
            assert node.has_attribute('alias'), """node.has_attribute('alias')"""
            assert name != node.get_attribute('alias'), """name != node.get_attribute('alias')"""
            return self.__getattr__(node.get_attribute('alias'))
        raise NotImplementedError('Get binding for "%s"' % name)

    @staticmethod
    def _has_c_type(name):
        return name in category_name_map['type'] or name in platform_types or name in native_types
    

    def get_constant_value(self, ctype: str, value):
        code = '%s value = %s;' % (ctype, value)
        code = self.preprocess_code(code)
        ast = self.cparser.parse(code)
        return self.get_const_value_ast(ast.ext[0].init)
    
    def get_const_value_ast(self, node: pycparser.c_ast.Node):
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
                return ~self.get_const_value_ast(node.expr)
            if node.op == '+':
                return +self.get_const_value_ast(node.expr)
            if node.op == '-':
                return -self.get_const_value_ast(node.expr)
        elif node_type is c_ast.BinaryOp:
            if node.op == '|':
                return self.get_const_value_ast(node.left) | self.get_const_value_ast(node.right)
            if node.op == '&':
                return self.get_const_value_ast(node.left) & self.get_const_value_ast(node.right)
            if node.op == '^':
                return self.get_const_value_ast(node.left) ^ self.get_const_value_ast(node.right)
            if node.op == '+':
                return self.get_const_value_ast(node.left) + self.get_const_value_ast(node.right)
            if node.op == '-':
                return self.get_const_value_ast(node.left) - self.get_const_value_ast(node.right)
            if node.op == '*':
                return self.get_const_value_ast(node.left) * self.get_const_value_ast(node.right)
            if node.op == '/':
                return self.get_const_value_ast(node.left) / self.get_const_value_ast(node.right)
            if node.op == '%':
                return self.get_const_value_ast(node.left) % self.get_const_value_ast(node.right)
            if node.op == '<<':
                return self.get_const_value_ast(node.left) << self.get_const_value_ast(node.right)
            if node.op == '>>':
                return self.get_const_value_ast(node.left) >> self.get_const_value_ast(node.right)
        elif node_type is c_ast.ID:
            if node.name not in category_name_map['define'] and node.name not in category_name_map['value']:
                raise self._cparser.ParseError('Missing ID: %s' % node.name)
            return self[node.name]
        elif node_type is c_ast.Cast:
            print('c_cast: %s' % node.to_type.type)
            return None
            # target_type = self.get_type_from_decl(node.to_type.type)
            # value = self.get_const_value_ast(node.expr)
            # return target_type.make_python_value(value)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)