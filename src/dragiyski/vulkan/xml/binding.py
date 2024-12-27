import sys, re, ast, ctypes, operator, pycparser.c_generator, pycparser.c_parser, pycparser.c_ast
from collections.abc import Mapping, Collection
from types import MappingProxyType
from logging import getLogger
from .taxonomy import Taxonomy
from .node import Node
from .c import CParser, CGenerator, CTypeInfo, c_native_types, c_external_types, c_boolean_operators, c_value_operators, c_type_category

logger = getLogger('dragiyski.vulkan.binding')

REGEXP_INT_WORD = re.compile(r'\bint\b')

class Binding:
    class DefinitionError(RuntimeError):
        pass

    class DuplicateDefinitionError(DefinitionError):
        pass

# Binding will directly bind vulkan names to ctypes.
# TODO: Create Api classes that accept binding and taxonomy
# TODO: Api classes can use both to generate more pythonic version of vulkan commands.
class LazyBinding(Binding):
    class CMacro:
        def __init__(self, binding: 'LazyBinding', name: str, template: list[str], arguments: list[str]):
            self.binding = binding
            self.template = template
            self.name = name
            if len(set(arguments)) != len(arguments):
                raise ValueError('Found duplicate argument names')
            self.arguments = arguments

        @property
        def __name__(self):
            return self.name

        def _convert_to_code(self, value):
            if isinstance(value, CGenerator.Code):
                return value
            value = CTypeInfo(value).get_value(value)
            if isinstance(value, (str, bytes)):
                return CGenerator.Code(CGenerator.generate_c_string(value))
            if isinstance(value, int):
                return CGenerator.Code('%d' % value)
            if isinstance(value, float):
                string = '%g' % value
                if '.' not in string:
                    string += '.0'
                return CGenerator.Code(string)
            raise NotImplementedError('No known method for converting "%s" to "CGenerator.Code"' % (value.__qualname__))
        
        def __call__(self, *args, **kwargs):
            context = {}
            for i in range(min(len(self.arguments), len(args))):
                context[self.arguments[i]] = self._convert_to_code(args[i])
            for name, value in kwargs.items():
                if name in context:
                    raise TypeError('%s() got multiple values for argument %r' % (self.name, name))
                context[name] = self._convert_to_code(value)
            missing = set(self.arguments).difference(context.keys())
            if len(missing) > 0:
                missing_list = [x for x in self.arguments if x in missing]
                raise TypeError('%s() missing %d required positional arguments:' % (self.name, len(missing_list), ', '.join(repr(x) for x in missing_list)))
            macro_args = [context[name] for name in self.arguments]
            macro_call = pycparser.c_ast.FuncCall(
                name=pycparser.c_ast.ID(name=self.name),
                args=pycparser.c_ast.ExprList(exprs=macro_args)
            )
            macro_decl = pycparser.c_ast.Decl(
                name='_',
                quals=[],
                align=[],
                storage=[],
                funcspec=[],
                bitsize=None,
                type=pycparser.c_ast.TypeDecl(
                    declname='_',
                    quals=[],
                    align=[],
                    type=pycparser.c_ast.IdentifierType(names=['int'])
                ),
                init=macro_call
            )
            macro_ast = pycparser.c_ast.FileAST(ext=[macro_decl])
            code = self.binding.c_generator.visit(macro_ast)
            ast_root = self.binding.c_preprocess_code(code)
            res_value = self.binding.c_get_ast_expr_node_value(ast_root.ext[0].init)
            return CTypeInfo(res_value).get_value(res_value)
            

    def __init__(self, taxonomy: Taxonomy, *, skip_names: Collection = set()):
        self.taxonomy = taxonomy

        # All types by both Vulkan and external
        self._types = {
            **c_native_types,
            **c_external_types
        }
        # All known values (both vulkan and external)
        self._values = {
            'VK_NULL_HANDLE': None,
            'VK_USE_64_BIT_PTR_DEFINES': ctypes.sizeof(ctypes.c_void_p) == 8
        }
        self._skip_names = set(skip_names) | {
            'VK_DEFINE_HANDLE',
            'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
        }
        self._names = set(self.taxonomy.nodes.keys()).difference(self._skip_names)
        self.c_pp_definitions = {}
        self.c_parser = CParser(self._types)
        self.c_generator = CGenerator()

        # Functional style macros use templates, while preprocessor macros are direct substitution
        for name in self.taxonomy.category['define']:
            if name in self._skip_names:
                continue
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.path[-2:] != ['types', 'type']:
                    continue
                try:
                    macro = CParser.parse_preprocessor(node.get_text())
                    if isinstance(macro, dict):
                        macro = self.CMacro(self, name, macro['template'], macro['arguments'])
                    self.c_pp_definitions[name] = macro
                except ValueError:
                    pass

    # def __dir__(self):
        # return object.__dir__(self) + list(self._names)
    
    # def __getattr__(self, name: str):
    #     try:
    #         return self.__getitem__(name)
    #     except KeyError:
    #         raise AttributeError(name)

    def __getitem__(self, name: str):
        if name in self._names:
            if name in self.__dict__:
                return self.__dict__[name]
            try:
                value = self._get_binding(name)
            except NotImplementedError:
                logger.warning(sys.exc_info(), exc_info=True)
                raise KeyError(name)
            self.__dict__[name] = value
            return value
        raise KeyError(name)
    
    def _get_binding(self, name):
        if name not in self._names or name in self._skip_names:
            raise KeyError(name)
        name = self._resolve_alias(name)
        if name in self.c_pp_definitions:
            return self.c_get_define_value(name)
        if name in self._types:
            return self._types[name]
        if name in self.taxonomy.category['basetype']:
            self._types[name] = self.c_get_basetype(name)
            return self._types[name]
        raise NotImplementedError('No vulkan binding for "%s"' % name)

    def _resolve_alias(self, name: str):
        while name in self.taxonomy.category['alias']:
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.has_attribute('alias'):
                    name = node.get_attribute('alias')
        return name
    
    def c_get_basetype(self, name: str):
        for node in self.taxonomy.nodes[name]:
            node: Node
            if node.path[-2:] == ['types', 'type'] and 'name' in node.children:
                words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in node.get_text_nodes_before(node.get('name'))]))]
                words = [x for x in words if x]
                if 'typedef' not in words:
                    if words[-1] in ['struct', 'union']:
                    # Opaque types are returned as None. While this is a bit hacky (as non-type values can also be None),
                    # it works with ctypes.POINTER, so it does not break 
                        return None
                    raise RuntimeError(f'At {node.file_path}: Basetype "{name}" not a typedef or struct/union!')
                words = words[len(words) - words[::-1].index('typedef'):]
                ctype = ' '.join(words).strip()
                ptr_count = 0
                while ctype.endswith('*'):
                    ctype = ctype[:-1].strip()
                    ptr_count += 1
                if 'struct' in words or 'union' in words:
                    ctype = None
                else:
                    ctype = self[ctype]
                while ptr_count > 0:
                    ctype = ctypes.POINTER(ctype)
                    ptr_count -= 1
                return ctype

    def c_preprocess_code(self, code: str):
        ast = self.c_parser.parse(code)
        while self.c_preprocess_ast_node(ast):
            code = self.c_generator.visit(ast)
            ast = self.c_parser.parse(code)
        return ast
    
    def c_preprocess_ast_node(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if isinstance(child_node, pycparser.c_ast.ID) and child_node.name in self.c_pp_definitions and isinstance(self.c_pp_definitions[child_node.name], str):
                setattr(node, name, self.c_generator.Code(self.c_pp_definitions[child_node.name]))
                has_substitution = True
                continue
            if isinstance(child_node, pycparser.c_ast.FuncCall) and child_node.name.name in self.c_pp_definitions and isinstance(self.c_pp_definitions[child_node.name.name], self.CMacro):
                args = [self.c_generator.visit(x) for x in child_node.args]
                macro = self.c_pp_definitions[child_node.name.name]
                if len(macro.arguments) != len(args):
                    raise pycparser.c_parser.ParseError('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro['arguments'], len(args))))
                code = []
                for part in macro.template:
                    if isinstance(part, str):
                        code.append(part)
                    elif part['string']:
                        code.append(self.c_generator.generate_c_string(args[part['index']]))
                    else:
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, self.c_generator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.c_preprocess_ast_node(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution
    
    def c_get_define_value(self, name):
        if name in self.c_pp_definitions:
            if isinstance(self.c_pp_definitions[name], str):
                c_ast = self.c_preprocess_code(f'int var = {name};')
                value = self.c_get_ast_expr_node_value(c_ast.ext[0].init)
                return CTypeInfo(value).get_value(value)
            if isinstance(self.c_pp_definitions[name], self.CMacro):
                return self.c_pp_definitions[name]

    @staticmethod
    def c_create_ctype_buffer_from_string(value: str):
        return ctypes.create_string_buffer(value.encode())

    def c_parse_string_literal_ctype(self, literal: str):
        start_index = 0
        method = self.c_create_ctype_buffer_from_string
        if literal.startswith('u8'):
            start_index = 2
        elif literal.startswith('L'):
            start_index = 1
            method = ctypes.create_unicode_buffer
        elif literal.startswith('U'):
            start_index = 1
            raise NotImplementedError('Unicode literals are not implemented by this CParser, yet')
        if (len(literal) - start_index) < 2 or literal[start_index] != '"' or literal[-1] != '"':
            raise ValueError('Invalid C literal: expected string literals to start and end with quote (")')
        value = self.c_parser.parse_c_string(literal[start_index+1:-1])
        return method(value)
    
    def c_get_ast_unary_operator(self, node: pycparser.c_ast.UnaryOp):
        arg = self.c_get_ast_expr_node_value(node.expr)
        arg_info = CTypeInfo(arg)
        arg_value = arg_info.get_value(arg)
        if isinstance(arg, (int, float, bool)):
            res_type = ctypes.c_bool if node.op in c_boolean_operators else arg_info.type
            res_value = c_value_operators['unary'][node.op](arg_value)
            return res_type(res_value)
        raise TypeError(f'Unary operation {node.op!r} not defined for argument of type {arg_info.type.__name__!r}')
    
    def c_get_ast_binary_operator(self, node: pycparser.c_ast.BinaryOp):
        left = self.c_get_ast_expr_node_value(node.left)
        right = self.c_get_ast_expr_node_value(node.right)
        left_info = CTypeInfo(left)
        right_info = CTypeInfo(right)
        left_value = left_info.get_value(left)
        right_value = right_info.get_value(right)
        # We do not know how to process any binary operations that are not on numbers:
        if isinstance(left_value, (int, float, bool)) and isinstance(right_value, (int, float, bool)):
            if node.op in c_boolean_operators:
                res_type = ctypes.c_bool
            else:
                res_size = max(left_info.size, right_info.size)
                if res_size > 0:
                    if left_info.is_float or right_info.is_float:
                        if res_size not in c_type_category['float']:
                            raise NotImplementedError(f'No operator {node.op!r} defined for types {left.__name__!r} and {right.__name__!r}')
                        res_type = c_type_category['float'][res_size]
                    elif left_info.is_unsigned or right_info.is_unsigned:
                        if res_size not in c_type_category['unsigned']:
                            raise NotImplementedError(f'No operator {node.op!r} defined for types {left.__name__!r} and {right.__name__!r}')
                        res_type = c_type_category['unsigned'][res_size]
                    else:
                        if res_size not in c_type_category['signed']:
                            raise NotImplementedError(f'No operator {node.op!r} defined for types {left.__name__!r} and {right.__name__!r}')
                        res_type = c_type_category['unsigned'][res_size]
                else:
                    if isinstance(left_value, float) or isinstance(right_value, float):
                        res_type = float
                    else:
                        assert isinstance(left_value, int), """isinstance(left_value, int)"""
                        assert isinstance(right_value, int), """isinstance(right_value, int)"""
                        res_type = int
            res_value = c_value_operators['binary'][node.op](left_value, right_value)
            return res_type(res_value)
        raise NotImplementedError(f'No operator {node.op!r} defined for types {left.__name__!r} and {right.__name__!r}')

    def c_get_ast_expr_node_value(self, node: pycparser.c_ast.Node):
        c_ast = pycparser.c_ast
        if isinstance(node, c_ast.Constant):
            if REGEXP_INT_WORD.search(node.type) is not None:
                return self._types[node.type](self.c_parser.parse_c_int(node.value))
            if node.type in ['float', 'double']:
                return self._types[node.type](self.c_parser.parse_c_float(node.value))
            if node.type == 'string':
                return self.c_parse_string_literal_ctype(node.value)
            raise NotImplementedError('TODO: C: Constant: %s' % node.type)
        if isinstance(node, c_ast.UnaryOp):
            return self.c_get_ast_unary_operator(node)
        if isinstance(node, c_ast.BinaryOp):
            return self.c_get_ast_binary_operator(node)
        if isinstance(node, c_ast.Cast):
            res_type = self.c_get_ast_type_from_decl(node.to_type.type)
            res_value = self.c_get_ast_expr_node_value(node.expr)
            res_value = CTypeInfo(res_value).get_value(res_value)
            return res_type(res_value)
        raise NotImplementedError(f'TODO: C: c_ast.{node.__name__}')
    
    def c_get_ast_type_from_decl(self, node: pycparser.c_ast.Node):
        c_ast = pycparser.c_ast
        if isinstance(node, c_ast.PtrDecl):
            return ctypes.POINTER(self.c_get_ast_type_from_decl(node.type))
        if isinstance(node, c_ast.ArrayDecl):
            length = self.get_ast_expr_node_value(node.dim)
            length = CTypeInfo(length).get_value(length)
            if not isinstance(length, int):
                raise TypeError('ArrayDecl length must be an integer')
            return self.c_get_ast_type_from_decl(node.type) * length
        if isinstance(node, c_ast.TypeDecl):
            if isinstance(node.type, pycparser.c_ast.IdentifierType):
                type_name = ' '.join(node.type.names)
            elif isinstance(node.type, (pycparser.c_ast.Struct, pycparser.c_ast.Union)):
                type_name = node.type.name
            else:
                raise NotImplementedError('TODO: C: TypeDecl => %s' % node.type.__name__)
            type_name = self._resolve_alias(type_name)
            # TODO: {
            # TODO: This must access to self[type_name] and then identify that returned value is type.
            try:
                self[type_name]
            except KeyError:
                pass
            if type_name not in self._types:
                raise pycparser.c_parser.ParseError('Reference to undefined type "%s"' % (type_name))
            assert CTypeInfo(self._types[type_name]).size > 0, """CTypeInfo(self._types[type]).size > 0"""
            return self._types[type_name]
            # TODO: }
        raise NotImplementedError(f'TODO: C: c_ast.{node.__name__}')