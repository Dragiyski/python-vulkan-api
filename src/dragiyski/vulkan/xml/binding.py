import sys, re, ast, ctypes, operator, pycparser.c_generator, pycparser.c_parser, pycparser.c_ast
from collections.abc import Mapping, Collection
from types import MappingProxyType
from logging import getLogger
from .taxonomy import Taxonomy
from .node import Node

def _c_sizeof(value):
    try:
        return ctypes.sizeof(value)
    except TypeError:
        return 0

def _c_division(left, right):
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        if isinstance(left, float) or isinstance(right, float):
            return left / right
        return left // right
    raise TypeError("unsupported operand type(s) for C-division: '%s' and '%s'" % (type(left).__name__, type(right).__name__))

unary_operation = {
    '~': operator.inv,
    '+': operator.pos,
    '-': operator.neg
}

binary_operation = {
    '|': operator.or_,
    '&': operator.and_,
    '^': operator.xor,
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': _c_division,
    '%': operator.mod,
    '<<': operator.lshift,
    '>>': operator.rshift
}

logger = getLogger('dragiyski.vulkan.binding')

REGEXP_MULTILINE_COMMENT = re.compile(r'\/\*.*\*\/')
REGEXP_SINGLELINE_COMMENT = re.compile(r'\/\/.*')
REGEXP_FUNC_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)')
REGEXP_VALUE_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\s+(.*)')

c_native_types = {
    'char': ctypes.c_char,
    'float': ctypes.c_float,
    'double': ctypes.c_double,
    'int8_t': ctypes.c_int8,
    'uint8_t': ctypes.c_uint8,
    'int16_t': ctypes.c_int16,
    'uint16_t': ctypes.c_uint16,
    'uint32_t': ctypes.c_uint32,
    'uint64_t': ctypes.c_uint64,
    'int32_t': ctypes.c_int32,
    'int64_t': ctypes.c_int64,
    'size_t': ctypes.c_size_t,
    'int': ctypes.c_int,
    'bool': ctypes.c_bool,
    'unsigned int': ctypes.c_uint,
    'unsigned long': ctypes.c_ulong,
    'unsigned long int': ctypes.c_ulong,
    'unsigned short': ctypes.c_ushort,
    'unsigned short int': ctypes.c_ushort,
    'unsigned char': ctypes.c_ubyte,
    'unsigned long long': ctypes.c_ulonglong,
    'unsigned long long int': ctypes.c_ulonglong,
    'int': ctypes.c_int,
    'long': ctypes.c_long,
    'long int': ctypes.c_long,
    'short': ctypes.c_short,
    'short int': ctypes.c_short,
    'long long': ctypes.c_longlong,
    'long long int': ctypes.c_longlong
}

c_external_types = {
    'VisualID': ctypes.c_uint32,  # X11/Xlib.h: CARD32
    'Window': ctypes.c_uint32,  # X11/Xlib.h: CARD32 => XID
    'RROutput': ctypes.c_uint32,  # X11/extensions/Xrandr.h
    'xcb_window_t': ctypes.c_uint32,  # xcb/xcb.h
    'xcb_visualid_t': ctypes.c_uint32, # xcb/xcb.h
    'HINSTANCE': ctypes.c_void_p,  # windows.h
    'HWND': ctypes.c_void_p,  # windows.h
    'HMONITOR': ctypes.c_void_p,  # windows.h
    'HANDLE': ctypes.c_void_p,  # windows.h
    'DWORD': ctypes.c_uint32,  # windows.h
    'LPCSTR': ctypes.c_char_p,  # windows.h
    'LPCTSTR': ctypes.c_char_p,  # windows.h
    'LPCWSTR': ctypes.c_wchar_p,  # windows.h
    'zx_handle_t': ctypes.c_uint32,  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': ctypes.c_uint32,  # Google games platform?
    'GgpFrameToken': ctypes.c_uint32,  # Google games platform?
    'NvSciSyncAttrList': ctypes.c_void_p, # NV Sci Platform
    'NvSciSyncObj': ctypes.c_void_p, # NV Sci Platform
    'NvSciSyncFence': ctypes.c_uint64 * 6, # NV Sci Platform
    'NvSciBufAttrList': ctypes.c_void_p, # NV Sci Platform
    'NvSciBufObj': ctypes.c_void_p, # NV Sci Platform
}

class CGenerator(pycparser.c_generator.CGenerator):
    """
    Same as pycparser.c_generator.CGenerator, but accept a special node CGenerator.Code that can substitute C code in the AST.
    """
    def visit_Code(self, node):
        return node.code
    
    class Code(pycparser.c_ast.Node):
        __slots__ = ('code', 'coord', '__weakref__')

        def __init__(self, code):
            self.code = code

class CParser(pycparser.CParser):
    def __init__(self, types: Mapping = {}, **kwargs):
        super().__init__(**kwargs)
        self._types = types
    
    def _lex_type_lookup_func(self, name):
        if super()._lex_type_lookup_func(name):
            return True
        return name in self._types
    
    @staticmethod
    def parse_c_int(value):
        match = re.match(r'(-?)0x([0-9A-Fa-f]+)', value)
        if match:
            return (-1 if len(match.group(1)) else 1) * int(match.group(2), 16)
        match = re.match(r'-?[0-9]+', value)
        if match:
            return int(match.group(0), 10)
        raise ValueError('Invalid integer value: %r' % value)
    
    @staticmethod
    def parse_c_float(value):
        match = re.match(r'-?[0-9]+(?:\.[0-9]+)?', value)
        if match:
            return float(match.group(0))
        raise ValueError('Invalid float value: %r' % value)
    
    @classmethod
    def parse_c_string(cls, value) -> str:
        if len(value) < 2 or value[0] != '"' or value[-1] != '"':
            raise ValueError('Invalid string value (missing open or close quotes): %s' % value)
        value = value[1:-1]

        value = re.sub(r'\\U([0-9A-Fa-f]{8})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{3})', cls.subst_unicode_oct, value)
        value = re.sub(r'\\(.)', cls.subst_slash_escape, value)
        return value
    
    @staticmethod
    def subst_unicode_hex(match):
        return chr(int(match.group(1), 16))


    @staticmethod
    def subst_unicode_oct(match):
        return chr(int(match.group(1), 8))


    @staticmethod
    def subst_string_unicode_char(match):
        char = match.group(0)
        code = ord(char)
        if code < 65535:
            return r'\u%04X' % code
        else:
            return r'\U%08X' % code

    @classmethod
    def subst_string_c_table(cls, match):
        char = match.group(0)
        code = ord(char)
        return '\\%s' % cls.subst_string_table[code]
    
    @classmethod
    def subst_slash_escape(cls, match):
        seq = match.group(1)
        if seq in cls.subst_table:
            return chr(cls.subst_table[seq])
        return match.group(0)

    subst_table = {
        'a': 0x07,
        'b': 0x08,
        'e': 0x1B,
        'f': 0x0C,
        'n': 0x0A,
        'r': 0x0D,
        't': 0x09,
        'v': 0x0B,
        '\\': 0x5C,
        "'": 0x27,
        '"': 0x22,
        '?': 0x3F,
    }

    subst_string_table = {v: k for k, v in subst_table.items()}
    REGEXP_SUBST_TABLE = re.compile('[%s]' % ''.join(r'\x%02X' % x for x in subst_table.values()))

    @classmethod
    def generate_c_string(cls, value: str):
        value = cls.REGEXP_SUBST_TABLE.sub(cls.subst_string_c_table, value)
        value = re.sub(r'[^\u0000-\u007F]', cls.subst_string_unicode_char, value)
        return '"%s"' % value

class Binding:
    class DefinitionError(RuntimeError):
        pass

    class DuplicateDefinitionError(DefinitionError):
        pass

# Binding will directly bind vulkan names to ctypes.
# TODO: Create Api classes that accept binding and taxonomy
# TODO: Api classes can use both to generate more pythonic version of vulkan commands.
class LazyBinding(Binding):
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
        # All names registered by Vulkan
        self._names = set(self.taxonomy.nodes.keys()).difference(self._skip_names)
        self.c_parser = CParser(types=MappingProxyType(self._types))
        self.c_generator = CGenerator()
        # Preprocessor definitions:
        self.pp_value_code = {}
        self.pp_func_code = {}

        # Functional style macros use templates, while preprocessor macros are direct substitution
        for name in self.taxonomy.category['define']:
            if name in self._skip_names:
                continue
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.path[-2:] != ['types', 'type']:
                    continue
                try:
                    self.c_preprocessor_define(node.get_text())
                except self.DefinitionError:
                    pass
        # Access to macros is as follows:
        # Functional style macros will generate FunctionMacro object whose __call__ will accept
        # named parameters (the macro names). Calling this function will accept both ctypes and python native types,
        # where the following types are accepted: int, float, bytes, str
        # With int/float can be converted to ctypes according to dedicated convertion principles.

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
        if name in self.pp_value_code:
            return self._resolve_pp_value_from_c_expression(self.pp_value_code[name])
        if name in self.pp_func_code:
            # pp_func_macro will result in a function taking parameter.
            # The function must convert python values to C as follows:
            # int => C constant int: example 23
            # float => C constant float: example 23.0
            # str => C constant string: example "Hello world!" (using UTF-8)
            # self.c_generator.Code => wraps str as C code for direct substitution
            # Once converted, the expression: <MACRO_NAME>(ARG_1, ARG_2,... ) will be created using the macro name
            # and converted arguments. Finally, the _resolve_pp_value_from_c_expression will be called with that expression,
            # to substitute the provided data and compute the final expression value.
            # Therefore, the "context" variable is not used here, as we do not expect IDs.
            # The "context" can still be used later for struct context in evaluation of altlen="..." attribute expressions
            return self._resolve_pp_func_from_c_expression(self.pp_func_code[name])
        raise NotImplementedError('No vulkan binding for "%s"' % name)
    
    def _resolve_pp_value_from_c_expression(self, c_expr: str):
        c_ast = self.c_preprocess_code_ast(f'int _ = {c_expr};')
        assert c_ast.__class__ is pycparser.c_ast.FileAST, """c_ast.__class__ is pycparser.c_ast.FileAST"""
        assert len(c_ast.ext) == 1, """len(c_ast.ext) == 1"""
        assert c_ast.ext[0].__class__ is pycparser.c_ast.Decl, """c_ast.ext[0].__class__ is pycparser.c_ast.Decl"""
        return self.c_ast_get_const_value(c_ast.ext[0].init).value
        pass
    
    def _c_get_value_from_ast(node: pycparser.c_ast.Node, context: Mapping = {}):
        pass

    def _resolve_alias(self, name: str):
        while name in self.taxonomy.category['alias']:
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.has_attribute('alias'):
                    name = node.get_attribute('alias')
        return name

    @staticmethod
    def c_get_preprocessor_lines(code):
        lines = []
        code = REGEXP_MULTILINE_COMMENT.sub('', code)
        code = code.splitlines()
        is_continuation_line = False
        for line in code:
            line = REGEXP_SINGLELINE_COMMENT.sub('', line)
            if len(line.strip()) <= 0:
                is_continuation_line = False
                continue
            if is_continuation_line:
                lines[-1] += ' ' + line
                if lines[-1].endswith('\\'):
                    lines[-1] = lines[-1][:-1]
                    is_continuation_line = True
                else:
                    is_continuation_line = False
            else:
                if line.endswith('\\'):
                    is_continuation_line = True
                    line = line[:-1]
                else:
                    is_continuation_line = False
                lines.append(line)
        return lines
    
    def c_preprocessor_define(self, code):
        code = self.c_get_preprocessor_lines(code)
        if len(code) != 1:
            raise self.DefinitionError('Unable to define macro with more than one preprocessor line.')
        code = code[0]
        is_func_macro = REGEXP_FUNC_MACRO.fullmatch(code)
        if is_func_macro is not None:
            return self._c_preprocessor_define_func_macro(is_func_macro)
        is_value_macro = REGEXP_VALUE_MACRO.fullmatch(code)
        if is_value_macro is not None:
            return self._c_preprocessor_define_value_macro(is_value_macro)
    
    def _c_preprocessor_define_func_macro(self, data: re.Match):
        name = data.group(1)
        arguments = [arg.strip() for arg in data.group(2).split(',')]
        code = data.group(3).strip()
        # This might not properly handle if argument name appear in a C string, but it is good enough for now.
        # pycparser.cparser cannot be used, as it does not handle #-prefix and ## operator
        words = [y for x in code.split('##') for y in re.split(r'\b', x)]
        template = []
        for word in words:
            if word in arguments:
                if len(template) > 0 and template[-1] == '#':
                    template[-1] = {
                        'name': word,
                        'index': arguments.index(word),
                        'string': True
                    }
                else:
                    template.append({
                        'name': word,
                        'index': arguments.index(word),
                        'string': False
                    })
            else:
                template.append(word)
        if name in self.pp_func_code or name in self.pp_value_code:
            raise self.DuplicateDefinitionError(f'Macro "{name}" already defined.')
        self.pp_func_code[name] = {
            'arguments': arguments,
            'template': template,
        }
    
    def _c_preprocessor_define_value_macro(self, data: re.Match):
        name = data.group(1)
        code = data.group(2)
        if name in self.pp_func_code or name in self.pp_value_code:
            raise self.DuplicateDefinitionError(f'Macro "{name}" already defined.')
        self.pp_value_code[name] = code

    def c_preprocess_code_ast(self, code: str):
        ast = self.c_parser.parse(code)
        while self.c_preprocess_ast(ast):
            code = self.c_generator.visit(ast)
            ast = self.c_parser.parse(code)
        return ast
    
    def c_preprocess_ast(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.pp_value_code:
                setattr(node, name, self.c_generator.Code(self.pp_value_code[child_node.name]))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.pp_func_code:
                args = [self.c_generator.visit(x) for x in child_node.args]
                macro = self.pp_func_code[child_node.name.name]
                if len(macro['arguments']) != len(args):
                    raise self.c_parser.ParseError('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro['arguments'], len(args))))
                code = []
                for part in macro['template']:
                    if isinstance(part, str):
                        code.append(part)
                    else:
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, self.c_generator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.c_preprocess_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution

    def c_parse(self, code):
        code = self.c_preprocess_code(code)
        return self.c_parser.parse(code)
    
    def get_python_code_for_func_macro(self, name):
        if name not in self.pp_func_code:
            raise KeyError('No function macro named "%s" exists.' % name)
        descriptor = self.pp_func_code[name]
        try:
            code = self.c_preprocess_code('int value = %s(%s);' % (name, ', '.join(descriptor['arguments'])))
        except pycparser.c_parser.ParseError:
            return None
        code_ast = self.c_parser.parse(code)
        c_ast = pycparser.c_ast
        assert type(code_ast) is c_ast.FileAST
        assert type(code_ast.ext[0]) is c_ast.Decl
        assert isinstance(code_ast.ext[0].init, c_ast.Node)
        opts = {}
        try:
            node = self._generate_python_ast_from_c_ast(code_ast.ext[0].init, descriptor['arguments'], opts)
        except NotImplementedError:
            return None
        return_node = ast.Return(node)
        body = [return_node]
        if 'use_ctypes' in opts:
            body.insert(0, ast.Import([ast.alias('ctypes')]))
        def_node = ast.FunctionDef(
            name=name,
            args=ast.arguments(
                args=[ast.arg(arg_name) for arg_name in descriptor['arguments']],
                posonlyargs=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]
            ),
            body=body,
            decorator_list=[],
            lineno=0,
            col_offset=0
        )
        return def_node
    
    def _generate_python_ast_from_c_ast(self, node: pycparser.c_ast.Node, args: list, opts: dict):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return ast.Constant(self.c_parser.parse_c_int(node.value))
            elif node.type in ['float', 'double']:
                return ast.Constant(self.c_parser.parse_c_float(node.value))
            elif node.type == 'string':
                return ast.Constant(self.c_parser.parse_c_string(node.value))
        elif node_type is c_ast.UnaryOp:
            if node.op == '~':
                return ast.UnaryOp(op=ast.Invert(), operand=self._generate_python_ast_from_c_ast(node.expr, args, opts))
            elif node.op == '+':
                return ast.UnaryOp(op=ast.UAdd(), operand=self._generate_python_ast_from_c_ast(node.expr, args, opts))
            elif node.op == '-':
                return ast.UnaryOp(op=ast.USub(), operand=self._generate_python_ast_from_c_ast(node.expr, args, opts))
        elif node_type is c_ast.BinaryOp:
            if node.op == '|':
                return ast.BinOp(op=ast.BitOr(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '&':
                return ast.BinOp(op=ast.BitAnd(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '^':
                return ast.BinOp(op=ast.BitXor(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '+':
                return ast.BinOp(op=ast.Add(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '-':
                return ast.BinOp(op=ast.Sub(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '*':
                return ast.BinOp(op=ast.Mult(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '/':
                return ast.BinOp(op=ast.Div(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '%':
                return ast.BinOp(op=ast.Mod(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '<<':
                return ast.BinOp(op=ast.LShift(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '>>':
                return ast.BinOp(op=ast.RShift(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
        elif node_type is c_ast.ID:
            if node.name not in args:
                raise pycparser.c_parser.ParseError('Missing ID: %s' % node.name)
            return ast.Name(id=node.name, ctx=ast.Load())
        elif node_type is c_ast.Cast:
            native_type = self.c_generator.visit(node.to_type.type)
            if native_type in c_native_types:
                value_node = self._generate_python_ast_from_c_ast(node.expr, args, opts)
                expr_node = ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='ctypes', ctx=ast.Load()),
                            attr=c_native_types[native_type].__name__,
                            ctx=ast.Load()
                        ),
                        args=[
                            value_node
                        ],
                        keywords=[]
                    ),
                    attr='value',
                    ctx=ast.Load()
                )
                opts['use_ctypes'] = True
                return expr_node
            raise NotImplementedError('Casting to type: %s' % node.to_type.type)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)
    
    def c_get_constant_value(self, value):
        code = 'int value = %s;' % (value)
        code = self.c_preprocess_code(code)
        ast = self.c_parser.parse(code)
        return self.c_get_const_value_ast(ast.ext[0].init)
    
    # Determining the result of binary operation depend on the operator
    # Rule 1: given two operands, always select the highest size type
    # Rule 2: given rule 1, if one of the types is unsigned integer, convert the other to unsigned if integer.
    # Rule 3: given rule 1, if one of the types is floating point, select floating point with at least the size of the integer.
    def c_ast_get_binary_type(self, left, right):
        try:
            left_size = ctypes.sizeof(left)
        except TypeError:
            left_size = 0
        try:
            right_size = ctypes.sizeof(right)
        except TypeError:
            right_size = 0
        max_size = max(left_size, right_size)
        left_value = left.value if hasattr(left, 'value') else None
        right_value = left.value if hasattr(left, 'value') else None
        if left_value is None and left_size == 0:
            left_value = left
        if right_value is None and right_size == 0:
            right_value = right
        floating_point = isinstance(left, float) or isinstance(right_value, float)
        if floating_point:
            if max_size == ctypes.sizeof(ctypes.c_longdouble):
                return ctypes.c_longdouble
            elif max_size == ctypes.sizeof(ctypes.c_double):
                return ctypes.c_double
            elif max_size == ctypes.sizeof(ctypes.c_float):
                return ctypes.c_float
            elif max_size == 0:
                return float
            raise NotImplementedError('No known binary operation between "%s" and "%s"' % (type(left).__name__, type(right).__name__))
        left_int = isinstance(left_value, int)
        right_int = isinstance(right_value, int)
        left_unsigned = left_int and left_size > 0 and type(left)(-1).value > 0
        right_unsigned = right_int and right_size > 0 and type(right)(-1).value > 0
        if left_unsigned or right_unsigned:
            if max_size == ctypes.sizeof(ctypes.c_uint64):
                return ctypes.c_uint64
            if max_size == ctypes.sizeof(ctypes.c_uint32):
                return ctypes.c_uint32
            if max_size == ctypes.sizeof(ctypes.c_uint16):
                return ctypes.c_uint16
            if max_size == ctypes.sizeof(ctypes.c_uint8):
                return ctypes.c_uint8
        if left_int and right_int:
            if left_size > right_size:
                return type(left)
            return type(right)
        raise NotImplementedError('No known binary operation between "%s" and "%s"' % (type(left).__name__, type(right).__name__))

    
    def c_ast_get_const_value(self, node: pycparser.c_ast.Node, context: Mapping = {}):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return self._types[node.type](self.c_parser.parse_c_int(node.value))
            elif node.type in ['float', 'double']:
                return self._types[node.type](self.c_parser.parse_c_float(node.value))
            elif node.type == 'string': # This is a special type contant, the actual type can be determined from prefix:
                if node.value.startswith('L"'):
                    return ctypes.c_wchar_p(self.c_parser.parse_c_string(node.value[1:]))
                elif node.value.startswith('U"'):
                    raise NotImplementedError('Unsupported C string prefix: U')
                    # return ctypes.create_string_buffer(self.c_parser.parse_c_string(node.value[1:]).encode(f'utf_32_{sys.byteorder[0]}e') + bytes([0] * 4))
                elif node.value.startswith('"'):
                    return ctypes.c_char_p(self.c_parser.parse_c_string(node.value).encode('utf-8'))
                else:
                    raise NotImplementedError('Unsupported C string prefix or separator')
        elif node_type is c_ast.UnaryOp:
            op = self.c_ast_get_const_value(node.value, context)
            op_value = op.value if hasattr(op, 'value') else op
            op_type = type(op)
            # TODO: negation (-) operator might promote unsigned into signed.
            return op_type(unary_operation[node.op](op_value))
            pass
        elif node_type is c_ast.BinaryOp:
            lop = self.c_ast_get_const_value(node.left, context)
            rop = self.c_ast_get_const_value(node.right, context)
            res_type = self.c_ast_get_binary_type(lop, rop)
            lop_value = lop.value if hasattr(lop, 'value') else lop
            rop_value = rop.value if hasattr(rop, 'value') else rop
            if node.op == '/':
                if isinstance(lop_value, int) and isinstance(rop_value, int):
                    res_value = lop_value // rop_value
                else:
                    res_value = lop_value / rop_value
            else:
                res_value = binary_operation[node.op](lop_value, rop_value)
            return res_type(res_value)
        elif node_type is c_ast.Cast:
            cast_value = self.c_ast_get_const_value(node.expr, context)
            cast_type = self.c_ast_get_type_from_decl(node.to_type.type)
            return cast_type(cast_value.value)
        elif node_type is c_ast.ID:
            # ID will be processed as follows:
            # from context, if specified - should be int, float, str or ctypes.* class
            # if not present in context, but hasattr(self, ID) is True, use that value
            raise NotImplementedError('TODO: ID Processing')
            # get_type_from_typedecl? In runtime this should obtain ctypes.* class
        raise NotImplementedError('TODO: C: Unsupported node type "%s"' % node_type.__name__)

    def c_ast_get_type_from_decl(self, node: pycparser.c_ast.Node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.PtrDecl:
            return ctypes.POINTER(self.c_ast_get_const_value(node.type))
        if node_type is c_ast.ArrayDecl:
            length = self.c_ast_get_const_value(node.dim).value
            return self.c_ast_get_const_value(node.type) * length
        if node_type is c_ast.TypeDecl:
            if type(node.type) is pycparser.c_ast.IdentifierType:
                type_name = ' '.join(node.type.names)
            elif type(node.type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union]:
                type_name = node.type.name
            else:
                raise NotImplementedError('TODO: C: TypeDecl => %s' % type(node.type).__name__)
            type_name = self._resolve_alias(type_name)
            if type_name not in self._types:
                raise pycparser.c_parser.ParseError('Reference to undefined type "%s"' % (type_name))
            return self._types[type_name]
        raise NotImplementedError('TODO: C: %s' % type(node).__name__)
            
    
    def c_get_const_value_ast(self, node: pycparser.c_ast.Node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return self.c_parser.parse_c_int(node.value)
            elif node.type in ['float', 'double']:
                return self.c_parser.parse_c_float(node.value)
            elif node.type == 'string':
                return self.c_parser.parse_c_string(node.value)
        elif node_type is c_ast.UnaryOp:
            match node.op:
                case '~':
                    return ~self.c_get_const_value_ast(node.expr)
                case '+':
                    return +self.c_get_const_value_ast(node.expr)
                case '-':
                    return -self.c_get_const_value_ast(node.expr)
        elif node_type is c_ast.BinaryOp:
            match node.op:
                case '|':
                    return self.c_get_const_value_ast(node.left) | self.c_get_const_value_ast(node.right)
                case '&':
                    return self.c_get_const_value_ast(node.left) & self.c_get_const_value_ast(node.right)
                case '^':
                    return self.c_get_const_value_ast(node.left) ^ self.c_get_const_value_ast(node.right)
                case '+':
                    return self.c_get_const_value_ast(node.left) + self.c_get_const_value_ast(node.right)
                case '-':
                    return self.c_get_const_value_ast(node.left) - self.c_get_const_value_ast(node.right)
                case '*':
                    return self.c_get_const_value_ast(node.left) * self.c_get_const_value_ast(node.right)
                case '/':
                    return self.c_get_const_value_ast(node.left) / self.c_get_const_value_ast(node.right)
                case '%':
                    return self.c_get_const_value_ast(node.left) % self.c_get_const_value_ast(node.right)
                case '<<':
                    return self.c_get_const_value_ast(node.left) << self.c_get_const_value_ast(node.right)
                case '>>':
                    return self.c_get_const_value_ast(node.left) >> self.c_get_const_value_ast(node.right)
        elif node_type is c_ast.ID:
            if node.name not in self.value_map:
                raise self.c_parser.ParseError('Missing ID: %s' % node.name)
            return self.value_map[node.name]['value']
        elif node_type is c_ast.Cast:
            native_type = self.c_generator.visit(node.to_type.type)
            if native_type in c_native_types:
                return c_native_types[native_type](self.c_get_const_value_ast(node.expr)).value
            raise NotImplementedError('Casting to type: %s' % node.to_type.type)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)