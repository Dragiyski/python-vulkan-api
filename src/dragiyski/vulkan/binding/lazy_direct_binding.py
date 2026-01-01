import sys
import re
import ctypes
import pycparser.c_parser
import pycparser.c_ast
from collections.abc import Collection
from collections import Counter, OrderedDict
from types import new_class
from logging import getLogger
from enum import IntFlag, IntEnum
from ..xml.taxonomy import Taxonomy
from ..xml.node import Node
from .c import CParser, CGenerator, CTypeInfo, c_native_types, c_external_types, c_boolean_operators, c_value_operators, c_type_category

logger = getLogger('dragiyski.vulkan.binding')

REGEXP_INT_WORD = re.compile(r'\bint\b')
REGEXP_C_AST_CHILD_NAME = re.compile(r'([a-zA-Z_][a-zA-Z0-9_]*)(?:\[([0-9+])\])?')


class _Alias:
    __slots__ = ('name', 'target')

    def __init__(self, name, target):
        self.name = name
        self.target = target


def _count_bits(value):
    bits = 0
    while value > 0:
        bits += value & 1
        value >>= 1
    return bits


def _key_value_bitmask_sort_key(item):
    return [_count_bits(item[1]), item[1]]


def _key_enum_sort_key(item):
    return item[1]


def _c_ast_set_attribute(target, name, value):
    if isinstance(name, int):
        target[name] = value
    pattern = REGEXP_C_AST_CHILD_NAME.fullmatch(name)
    if pattern is None:
        raise AttributeError(target, name)
    index = pattern.group(2)
    if index is not None:
        if len(index) > 0:
            index = int(index, 10)
        else:
            index = None
    if index is not None:
        getattr(target, pattern.group(1))[index] = value
    else:
        setattr(target, pattern.group(1), value)


class LazyDirectBinding:
    class CFunctionMacro:
        __slots__ = ('binding', 'template', 'name', 'arguments', '__weakref__')

        def __init__(self, binding: 'LazyDirectBinding', name: str, template: list[str | dict], arguments: list[str]):
            if len(set(arguments)) != len(arguments):
                duplicates = ', '.join(repr(x) for x in sorted(name for name, count in Counter(arguments) if count > 1))
                raise ValueError(f'In macro {name}, Found duplicate argument names: {duplicates}')
            self.binding = binding
            self.template = template
            self.arguments = arguments
            self.name = name

        def __repr__(self):
            return f'<{self.__qualname__} ({self.name}) object at {hex(id(self))}>'

        def _convert_to_code(self, value):
            if isinstance(value, self.binding._c_generator.Code):
                return value
            value = CTypeInfo(value).get_value(value)
            if isinstance(value, (str, bytes)):
                return self.binding._c_generator.Code(self.binding._c_generator.generate_c_string(value))
            if isinstance(value, int):
                return self.binding._c_generator.Code('%d' % value)
            if isinstance(value, float):
                string = '%g' % value
                if '.' not in string:
                    string += '.0'
                return self.binding._c_generator.Code(string)
            raise NotImplementedError('No known method for converting "%s" to "CGenerator.Code"' % (value.__qualname__))

        def __repr__(self):
            args = ', '.join(self.arguments)
            return f'<#define {self.name}({args}) object at {hex(id(self))}>'

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
            code = self.binding._c_generator.visit(macro_ast)
            ast_root = self.binding._c_preprocess_code(code)
            res_value = self.binding._c_get_ast_expr_node_value(ast_root.ext[0].init)
            return CTypeInfo(res_value).get_value(res_value)

    class LazyCType:
        __slots__ = ('binding', 'name', '_cached', '_value', '__weakref__')

        def __init__(self, binding, name):
            self.binding = binding
            self.name = name
            self._cached = False

        @property
        def ctype(self):
            if self._cached:
                return self._value
            self._value = self.binding._get_ctype(self.name)
            self._cached = True
            return self._value

    class KnownCType:
        __slots__ = ('ctype')

        def __init__(self, ctype):
            self.ctype = ctype

    class ComplexResolveContext:
        __slots__ = ('binding', 'name')

        def __init__(self, binding, name):
            self.binding = binding
            self.name = name

        def __enter__(self):
            self.binding._resolve_complex_type_enter(self.name)

        def __exit__(self, exc_type, exc_value, traceback):
            self.binding._resolve_complex_type_exit(self.name)

    __slots__ = (
        'taxonomy',
            '_skip_names', 
            '_names', 
            '_c_preprocessor_value', 
            '_c_preprocessor_macro', 
            '_c_types', 
            '_c_lazy_types', 
            '_c_complex_resolve_stack', 
            '_c_complex_resolve_set', 
            '_c_parser', 
            '_c_generator', 
            'VKAPI_PTR',
            '__dict__', 
            '__weakref__'
        )

    def __init__(self, taxonomy: Taxonomy, *, skip_names: Collection = ()):
        self.taxonomy = taxonomy
        self.VKAPI_PTR = ctypes.WINFUNCTYPE if (hasattr(ctypes, 'WINFUNCTYPE') and callable(ctypes.WINFUNCTYPE)) else ctypes.CFUNCTYPE
        self._c_preprocessor_macro = {}
        self._c_preprocessor_value = {}
        self._c_types = {
            **{k: self.KnownCType(v) for k, v in c_native_types.items()},
            **{k: self.KnownCType(v) for k, v in c_external_types.items()}
        }
        self._skip_names = set(skip_names) | {
            'VK_DEFINE_HANDLE',
            'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
        }

        # Skip VkStructureType values that refer to types node included in the current API.
        skip_callbacks = set()
        skip_structure_types = {member_node.get_attribute('values') for name in taxonomy.category['complex'] for node in taxonomy.nodes[name] for member_node in node.get_all('member') if 'name' in member_node.children and member_node.get('name').get_text() == 'sType' and member_node.has_attribute('values')}.difference(taxonomy.group_value_map['VkStructureType'])
        skip_structures = {name for name in taxonomy.category['complex'] for node in taxonomy.nodes[name] for member_node in node.get_all('member') if 'name' in member_node.children and member_node.get('name').get_text() == 'sType' and member_node.has_attribute('values') and member_node.get_attribute('values') in skip_structure_types}
        skip_structures_len = len(skip_structures)
        while True:
            skip_callbacks |= {name for name in self.taxonomy.category['callback'] for node in self.taxonomy.nodes[name] for type_node in node.get_all('type') if type_node.get_text() in skip_structures}
            skip_structures |= {name for name in taxonomy.category['complex'] for node in taxonomy.nodes[name] for member_node in node.get_all('member') if 'type' in member_node.children and (member_node.get('type').get_text() in skip_structure_types or member_node.get('type').get_text() in skip_callbacks)}
            if skip_structures_len == len(skip_structures):
                break
            skip_structures_len = len(skip_structures)
        skip_structure_callback = skip_structures | skip_callbacks
        skip_commands = set()
        for command_name, command_node in ((name, node) for name in self.taxonomy.category['command'] for node in self.taxonomy.nodes[name] if 'proto' in node.children):
            command_types = set([command_node.get('proto').get('type').get_text()]) | {param_node.get('type').get_text() for param_node in command_node.get_all('param')}
            if len(command_types & skip_structure_callback) > 0:
                skip_commands.add(command_name)
        self._skip_names |= skip_callbacks
        self._skip_names |= skip_commands
        self._skip_names |= skip_structures
        self._skip_names |= {x[4:] for x in skip_callbacks if x.startswith('PFN_')}

        for category in ['basetype', 'external_type', 'type', 'bitmask', 'enum', 'complex', 'command']:
            self._c_types.update({k: self.LazyCType(self, k) for k in self.taxonomy.category[category].difference(self._c_types.keys()).difference(self._skip_names)})
        callback_names = {x[4:] if x.startswith('PFN_') else x for x in self.taxonomy.category['callback']}
        self._c_types.update({k: self.LazyCType(self, k) for k in callback_names.difference(self._c_types.keys()).difference(self._skip_names)})
        self._c_parser = CParser(self._c_types.keys(), self._is_c_type)
        self._c_generator = CGenerator()
        self._c_complex_resolve_stack = []
        self._c_complex_resolve_set = set()
        pass

        self._names = set(self.taxonomy.nodes.keys()).difference(self._skip_names)
        pfn_names = {x for x in self._names.intersection(self.taxonomy.category['callback']) if x.startswith('PFN_')}
        self._names = self._names.difference(pfn_names).union({x[4:] for x in pfn_names})

        self._c_init_preprocessor()
        self._vulkan_init_handles()

    def __contains__(self, name: str):
        return name in self._names

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

    def _resolve_alias(self, name: str):
        while name in self.taxonomy.category['alias']:
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.has_attribute('alias'):
                    name = node.get_attribute('alias')
        return name

    def _get_binding(self, name):
        if name not in self._names or name in self._skip_names:
            raise KeyError(name)
        name = self._resolve_alias(name)
        if name in self._c_preprocessor_value:
            c_ast = self._c_preprocess_code(f'int _ = {name};')
            c_value = self._c_get_ast_expr_node_value(c_ast.ext[0].init)
            return CTypeInfo(c_value).get_value(c_value)
        if name in self._c_preprocessor_macro:
            return self._c_preprocessor_macro[name]
        if name in self.taxonomy.category['bitmask']:
            return self._vulkan_compile_bitmask(name)
        if name in self.taxonomy.category['enum']:
            return self._vulkan_compile_enum(name)
        if name in self.taxonomy.value_group_map:
            group_name = self.taxonomy.value_group_map[name]
            if group_name in self.taxonomy.bit_group_map:
                group_name = self.taxonomy.bit_group_map[group_name]
            return self[group_name][name]
        if name in self._c_types:
            return self._c_types[name].ctype
        if name in self.taxonomy.category['handle']:
            return self._c_types[name].ctype
        if name in self.taxonomy.category['value']:
            return self._vulkan_compile_value(name)

    def _get_ctype(self, name):
        name = self._resolve_alias(name)
        if name in self.taxonomy.category['basetype']:
            return self._c_resolve_base_type(name)
        if name in self.taxonomy.category['external_type']:
            return None
        if name in self.taxonomy.category['bitmask'] or name in self.taxonomy.category['enum']:
            ctype = self._c_types['int'].ctype
            for node in self.taxonomy.nodes[name]:
                if 'type' in node.children:
                    node_ctype = node.get('type').get_text()
                    assert node_ctype in self._c_types
                    ctype = self._c_types[node_ctype].ctype
            return ctype
        if name in self.taxonomy.category['complex']:
            return self._resolve_complex_type(name)
        if name in self.taxonomy.category['callback'] or f'PFN_{name}' in self.taxonomy.category['callback']:
            return self._resolve_callback_type(name[4:] if name.startswith('PFN_') else name)
        if name in self.taxonomy.category['command']:
            return self._resolve_command_type(name)
        raise NotImplementedError(f'No known method for resolving type "{name}"')
    
    def _is_c_type(self, name):
        if name.startswith('PFN_'):
            return name in self.taxonomy.category['callback']
        return False

    def _resolve_callback_type(self, name):
        node_name = 'PFN_' + name if 'PFN_' + name in self.taxonomy.nodes else name
        for node in self.taxonomy.nodes[node_name]:
            node: Node
            c_code = node.get_text()
            if c_code.startswith('typedef '):
                c_code = re.sub(r'\bVKAPI_PTR\b', '', c_code)
                c_ast = self._c_preprocess_code(c_code)
                assert isinstance(c_ast.ext[0], pycparser.c_ast.Typedef), """isinstance(c_ast.ext[0], pycparser.c_ast.Typedef)"""
                assert isinstance(c_ast.ext[0].type, pycparser.c_ast.PtrDecl), """isinstance(c_ast.ext[0].type, pycparser.c_ast.PtrDecl)"""
                assert isinstance(c_ast.ext[0].type.type, pycparser.c_ast.FuncDecl), """isinstance(c_ast.ext[0].type.type, pycparser.c_ast.FuncDecl)"""
                c_ast_func = c_ast.ext[0].type.type
                ret_type = self._c_get_ast_type_from_decl(c_ast_func.type)
                arg_types = [self._c_get_ast_type_from_decl(arg.type) for arg in c_ast_func.args.params]
                if len(arg_types) == 1 and arg_types[0] is None:
                    arg_types = []
                return self.VKAPI_PTR(ret_type, *arg_types)
        raise KeyError(name)
    
    def _resolve_command_type(self, name):
        node_name = 'PFN_' + name if 'PFN_' + name in self.taxonomy.nodes else name
        for node in self.taxonomy.nodes[node_name]:
            node: Node
            if 'proto' in node.children:
                proto = node.get('proto')
                ret_type = self._c_resolve_type(proto.get_text_before(proto.get('name')))
                arg_types = [self._c_resolve_type(arg.get_text_before(arg.get('name'))) for arg in node.get_all('param')]
                return self.VKAPI_PTR(ret_type, *arg_types)
        raise KeyError(name)
    
    def _c_resolve_type(self, type_code):
        c_code = f'typedef {type_code} _;'
        c_ast = self._c_preprocess_code(c_code)
        return self._c_get_ast_type_from_decl(c_ast.ext[0].type)
    
    def _resolve_complex_type(self, name):
        if name not in self._c_complex_resolve_set:
            with self.ComplexResolveContext(self, name):
                for node in self.taxonomy.nodes[name]:
                    node: Node
                    if 'member' in node.children:
                        for member_node in node.get_all('member'):
                            if 'type' in member_node.children:
                                member_type = member_node.get('type').get_text()
                                if member_type in self.taxonomy.category['complex']:
                                    self._resolve_complex_type(member_type)
        if name in self.taxonomy.category['struct']:
            BaseClass = ctypes.Structure
        elif name in self.taxonomy.category['union']:
            BaseClass = ctypes.Union
        else:
            raise RuntimeError(f'Unknown complex type category: {name}')
        Type = new_class(name, (BaseClass,), None, self._init_complex_type)
        self._c_types[name] = self.KnownCType(Type)
        if len(self._c_complex_resolve_stack) == 0:
            self._c_resolve_all_complex_type_fields()
        return Type

    def _init_complex_type(self, namespace):
        namespace['__module__'] = self.__module__

    def _c_init_preprocessor(self):
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
                        self._c_preprocessor_macro[name] = self.CFunctionMacro(self, name, macro['template'], macro['arguments'])
                    else:
                        self._c_preprocessor_value[name] = macro
                except ValueError:
                    pass

    def _vulkan_init_handles(self):
        handle_ctype = {
            'VK_DEFINE_HANDLE': ctypes.c_void_p,
            'VK_DEFINE_NON_DISPATCHABLE_HANDLE': ctypes.c_void_p if ctypes.sizeof(ctypes.c_void_p) == 8 else ctypes.c_uint64
        }
        self.__dict__['VK_NULL_HANDLE'] = 0
        for name in self.taxonomy.category['handle']:
            for node in self.taxonomy.nodes[name]:
                if node.get_attribute('category') == 'handle' and not node.has_attribute('alias') and node.has_attribute('objtypeenum') and 'type' in node.children and 'name' in node.children:
                    assert node.get('name').get_text() == name, """node.get('name').get_text() == name"""
                    self._c_types[name] = self.KnownCType(handle_ctype[node.get('type').get_text()])

    def _c_preprocess_code(self, code: str):
        ast = self._c_parser.parse(code)
        while self._c_preprocess_ast_node(ast):
            code = self._c_generator.visit(ast)
            ast = self._c_parser.parse(code)
        return ast

    def _c_preprocess_ast_node(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if isinstance(child_node, pycparser.c_ast.ID) and child_node.name in self._c_preprocessor_value:
                _c_ast_set_attribute(node, name, self._c_generator.Code(self._c_preprocessor_value[child_node.name]))
                has_substitution = True
                continue
            if isinstance(child_node, pycparser.c_ast.FuncCall) and child_node.name.name in self._c_preprocessor_macro:
                assert isinstance(self._c_preprocessor_macro[child_node.name.name], self.CFunctionMacro), """isinstance(self._c_preprocessor_macro[child_node.name.name], self.CFunctionMacro)"""
                args = [self._c_generator.visit(x) for x in child_node.args]
                macro = self._c_preprocessor_macro[child_node.name.name]
                macro: 'LazyDirectBinding.CFunctionMacro'
                if len(macro.arguments) != len(args):
                    raise pycparser.c_parser.ParseError('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro.arguments), len(args)))
                code = []
                for part in macro.template:
                    if isinstance(part, str):
                        code.append(part)
                    elif part['string']:
                        code.append(self._c_generator.generate_c_string(args[part['index']]))
                    else:
                        code.append(args[part['index']])
                code = ''.join(code)
                _c_ast_set_attribute(node, name, self._c_generator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self._c_preprocess_ast_node(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution

    @staticmethod
    def _c_create_ctype_buffer_from_string(value: str):
        return ctypes.create_string_buffer(value.encode())

    def _c_parse_string_literal_ctype(self, literal: str):
        start_index = 0
        method = self._c_create_ctype_buffer_from_string
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
        value = self._c_parser.parse_c_string(literal[start_index+1:-1])
        return method(value)

    def _c_get_ast_unary_operator(self, node: pycparser.c_ast.UnaryOp):
        arg = self._c_get_ast_expr_node_value(node.expr)
        arg_info = CTypeInfo(arg)
        arg_value = arg_info.get_value(arg)
        if isinstance(arg_value, (int, float, bool)):
            res_type = ctypes.c_bool if node.op in c_boolean_operators else arg_info.type
            res_value = c_value_operators['unary'][node.op](arg_value)
            return res_type(res_value)
        raise TypeError(f'Unary operation {node.op!r} not defined for argument of type {arg_info.type.__name__!r}')

    def _c_get_ast_binary_operator(self, node: pycparser.c_ast.BinaryOp):
        left = self._c_get_ast_expr_node_value(node.left)
        right = self._c_get_ast_expr_node_value(node.right)
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

    def _c_get_ast_expr_node_value(self, node: pycparser.c_ast.Node):
        if isinstance(node, pycparser.c_ast.Constant):
            if REGEXP_INT_WORD.search(node.type) is not None:
                return self._c_types[node.type].ctype(self._c_parser.parse_c_int(node.value))
            if node.type in ['float', 'double']:
                return self._c_types[node.type].ctype(self._c_parser.parse_c_float(node.value))
            if node.type == 'string':
                return self._c_parse_string_literal_ctype(node.value)
            raise NotImplementedError('TODO: C: Constant: %s' % node.type)
        if isinstance(node, pycparser.c_ast.UnaryOp):
            return self._c_get_ast_unary_operator(node)
        if isinstance(node, pycparser.c_ast.BinaryOp):
            return self._c_get_ast_binary_operator(node)
        if isinstance(node, pycparser.c_ast.Cast):
            res_type = self._c_get_ast_type_from_decl(node.to_type.type)
            res_value = self._c_get_ast_expr_node_value(node.expr)
            res_value = CTypeInfo(res_value).get_value(res_value)
            return res_type(res_value)
        if isinstance(node, pycparser.c_ast.ID) and node.name in self.taxonomy.category['value']:
            return self[node.name]
        raise NotImplementedError(f'TODO: C: pycparser.c_ast.{node.__name__}')

    def _c_get_ast_type_from_decl(self, node: pycparser.c_ast.Node):
        c_ast = pycparser.c_ast
        if isinstance(node, c_ast.PtrDecl):
            ptr_type = self._c_get_ast_type_from_decl(node.type)
            if ptr_type is ctypes.c_char:
                return ctypes.c_char_p
            if ptr_type is ctypes.c_wchar:
                return ctypes.c_wchar_p
            return ctypes.POINTER(ptr_type)
        if isinstance(node, c_ast.ArrayDecl):
            length = self._c_get_ast_expr_node_value(node.dim)
            length = CTypeInfo(length).get_value(length)
            if not isinstance(length, int):
                raise TypeError('ArrayDecl length must be an integer')
            return self._c_get_ast_type_from_decl(node.type) * length
        if isinstance(node, c_ast.TypeDecl):
            if isinstance(node.type, pycparser.c_ast.IdentifierType):
                type_name = ' '.join(node.type.names)
            elif isinstance(node.type, (pycparser.c_ast.Struct, pycparser.c_ast.Union)):
                type_name = node.type.name
            else:
                raise NotImplementedError('TODO: C: TypeDecl => %s' % node.type.__name__)
            type_name = self._resolve_alias(type_name)
            if type_name.startswith('PFN_'):
                type_name = type_name[4:]
            if type_name not in self._c_types:
                raise pycparser.c_parser.ParseError('Reference to undefined type "%s"' % (type_name))
            c_type = self._c_types[type_name].ctype
            assert c_type is None or issubclass(c_type, (ctypes.Structure, ctypes.Union)) or CTypeInfo(c_type).size > 0, """c_type is None or issubclass(c_type, (ctypes.Structure, ctypes.Union)) or CTypeInfo(c_type).size > 0"""
            return c_type
        raise NotImplementedError(f'TODO: C: c_ast.{node.__name__}')

    def _c_resolve_base_type(self, name):
        for node in self.taxonomy.nodes[name]:
            node: Node
            if node.path[-2:] == ['types', 'type'] and 'name' in node.children:
                name_node = node.get('name')
                c_expr = node.get_text_before(name_node).split('\n')[-1] + name_node.get_text() + node.get_text_after(name_node).split('\n')[0]
                c_ast = self._c_preprocess_code(c_expr).ext[0]
                if isinstance(c_ast, pycparser.c_ast.Typedef):
                    assert c_ast.name == name, """c_ast.name == name"""
                    return self._c_get_ast_type_from_decl(c_ast.type)
                if isinstance(c_ast, pycparser.c_ast.Decl):
                    if isinstance(c_ast.type, (pycparser.c_ast.Struct, pycparser.c_ast.Union)):
                        assert c_ast.type.name == name, """c_ast.name == name"""
                        # Declaration of opaque strucutre: ctypes.POINTER(None) will return ctypes.c_void_p
                        return None
                raise NotImplementedError(f'Cannot handle the following C expression: {c_expr}')
        raise KeyError(name)

    def _vulkan_compile_bitmask(self, name: str):
        alias_map = {}
        value_map = {}
        if name in self.taxonomy.group_bit_map:
            bits_name = self.taxonomy.group_bit_map[name]
            if bits_name in self.taxonomy.group_value_map:
                bit_values = self.taxonomy.group_value_map[bits_name]
                for bit_name in bit_values:
                    value = self._get_vulkan_value(bit_name)
                    if isinstance(value, _Alias):
                        assert value.name == bit_name, """value.name == bit_name"""
                        if value.name not in alias_map:
                            alias_map[value.name] = value.target
                        elif alias_map[value.name] != value.target:
                            raise ValueError(f'Invalid alias: {value.name} already points to {alias_map[value.name]}, but a second declaration points to {value.target}')
                    else:
                        value_map[bit_name] = value
        bitmask_class = new_class(name, (IntFlag,), None, lambda ns: ns.update(OrderedDict(sorted(value_map.items(), key=_key_value_bitmask_sort_key))))
        for bit_name, value in alias_map.items():
            setattr(bitmask_class, bit_name, bitmask_class[value])
            bitmask_class._member_map_[bit_name] = bitmask_class[value]
        return bitmask_class

    def _vulkan_compile_enum(self, name: str):
        alias_map = {}
        value_map = {}
        if name in self.taxonomy.group_value_map:
            enum_values = self.taxonomy.group_value_map[name]
            for enum_value_name in enum_values:
                value = self._get_vulkan_value(enum_value_name)
                if isinstance(value, _Alias):
                    assert value.name == enum_value_name, """value.name == bit_name"""
                    if value.name not in alias_map:
                        alias_map[value.name] = value.target
                    elif alias_map[value.name] != value.target:
                        raise ValueError(f'Invalid alias: {value.name} already points to {alias_map[value.name]}, but a second declaration points to {value.target}')
                else:
                    value_map[enum_value_name] = value
        enum_class = new_class(name, (IntEnum,), None, lambda ns: ns.update(OrderedDict(sorted(value_map.items(), key=_key_enum_sort_key))))
        for enum_value_name, value in alias_map.items():
            setattr(enum_class, enum_value_name, enum_class[value])
            enum_class._member_map_[enum_value_name] = enum_class[value]
        return enum_class

    def _vulkan_compile_value(self, name):
        value = self._get_vulkan_value(name)
        return value
        pass

    def _resolve_complex_type_enter(self, name):
        if name in self._c_complex_resolve_stack:
            raise RuntimeError(f'Cyclic reference detected: {name}')
        self._c_complex_resolve_set.add(name)
        self._c_complex_resolve_stack.append(name)

    def _resolve_complex_type_exit(self, name):
        if self._c_complex_resolve_stack[-1] != name:
            raise RuntimeError(f'Complex type stack mismatch: {name} != {self._c_complex_resolve_stack[-1]}')
        self._c_complex_resolve_stack.pop()

    def _c_resolve_all_complex_type_fields(self):
        for name in self._c_complex_resolve_set:
            self._c_resolve_complex_type_fields(name)
        self._c_complex_resolve_set.clear()
    
    def _c_resolve_complex_type_fields(self, name):
        c_code = ''
        if name in self.taxonomy.category['struct']:
            c_code += 'struct'
        elif name in self.taxonomy.category['union']:
            c_code += 'union'
        else:
            raise RuntimeError(f'Unknown complex type category: {name}')
        c_code += ' %s {' % name
        c_code = [c_code]
        for node in self.taxonomy.nodes[name]:
            node: Node
            if 'member' in node.children:
                for member_node in node.get_all('member'):
                    c_code.append('    %s;' % member_node.get_text())
        c_code.append('};')
        c_ast = self._c_preprocess_code('\n'.join(c_code))
        fields = []
        for decl in c_ast.ext[0].type.decls:
            if decl.bitsize is not None:
                field = (decl.name, self._c_get_ast_type_from_decl(decl.type), decl.bitsize)
            else:
                field = (decl.name, self._c_get_ast_type_from_decl(decl.type))
            fields.append(field)
        self._c_types[name].ctype._fields_ = fields


    def _get_vulkan_value(self, value_name: str):
        for node in self.taxonomy.nodes[value_name]:
            node: Node
            factor = 1
            if node.get_attribute('dir') == '-':
                factor = -1
            if node.has_attribute('alias'):
                assert factor == 1, """factor == 1"""
                return _Alias(value_name, self._resolve_alias(value_name))
            if node.has_attribute('bitpos'):
                assert factor == 1, """factor == 1"""
                bitpos = self._c_parser.parse_c_int(node.get_attribute('bitpos'))
                return 1 << bitpos
            if node.has_attribute('value'):
                code = self._c_preprocess_code(f'int _ = {node.get_attribute('value')};')
                value = self._c_get_ast_expr_node_value(code.ext[0].init)
                value = CTypeInfo(value).get_value(value)
                if isinstance(value, (int, float)):
                    return factor * value
                assert factor == 1, """factor == 1"""
                return value
            if node.has_attribute('offset'):
                if not node.has_attribute('extnumber'):
                    assert 'extension' in node.path, """'extension' in node.path"""
                    extension_node = node
                    while extension_node is not None and extension_node.path[-1] != 'extension':
                        extension_node = extension_node.parent_node
                    assert extension_node is not None and extension_node.has_attribute('number'), """extension_node is not None and extension_node.has_attribute('number')"""
                    extnumber = self._c_parser.parse_c_int(extension_node.get_attribute('number'))
                else:
                    extnumber = self._c_parser.parse_c_int(node.get_attribute('extnumber'))
                offset = self._c_parser.parse_c_int(node.get_attribute('offset'))
                return factor * (1000000000 + (extnumber - 1) * 1000 + offset)
        raise NotImplementedError(f'Bitmask node {value_name} has no sufficient information for determining its value.')
