import re, math, ctypes, operator, pycparser.c_ast, pycparser.c_generator
from collections.abc import Mapping
from functools import cached_property

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

c_type_category = {
    'signed': {
        1: ctypes.c_int8,
        2: ctypes.c_int16,
        4: ctypes.c_int32,
        8: ctypes.c_int64
    },
    'unsigned': {
        1: ctypes.c_uint8,
        2: ctypes.c_uint16,
        4: ctypes.c_uint32,
        8: ctypes.c_uint64
    },
    'float': {
        ctypes.sizeof(ctypes.c_float): ctypes.c_float,
        ctypes.sizeof(ctypes.c_double): ctypes.c_double,
    }
}

if ctypes.sizeof(ctypes.c_longdouble) not in c_type_category['float']:
    c_type_category['float'][ctypes.sizeof(ctypes.c_longdouble)] = ctypes.c_longdouble

def c_operator_div(left, right):
    if isinstance(left, float) or isinstance(right, float):
        return left / right
    return left // right

def c_boolean_and(left, right):
    return bool(left) and bool(right)

def c_boolean_or(left, right):
    return bool(left) or bool(right)

def c_increment(value):
    return value + 1

def c_decrement(value):
    return value - 1

def c_idle(value):
    return value

c_value_operators = {
    'unary': {
        '+': operator.pos,
        '-': operator.neg,
        '~': operator.inv,
        '!': operator.not_,
        '++': c_increment,
        '--': c_decrement,
        # We do not actually execute code. We do not care about future or previous expressions or memory/variable state.
        # Instead we just get the value of a single expression.
        # The the increment effect of ++X and X++ is ignored.
        # Only the expression value of (++X) and (X++) matters. (X++) will be same as X prior the increment, thus X++, and X-- postfix have no visible effects.
        'p++': c_idle,
        'p--': c_idle,
    },
    'binary': {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': c_operator_div,
        '%': operator.mod,
        '^': operator.xor,
        '&': operator.and_,
        '|': operator.or_,
        '&&': c_boolean_and,
        '||': c_boolean_or,
        '==': operator.eq,
        '!=': operator.neq,
        '<': operator.lt,
        '<=': operator.le,
        '>': operator.gt,
        '>=': operator.ge,
        '<<': operator.lshift,
        '>>': operator.rshift
    }
}

c_boolean_operators = { '!', '&&', '||', '==', '!=', '<', '>', '<=', '>=' }

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

class CTypeInfo:
    _instance = {}

    def __new__(cls, ctype):
        if not isinstance(ctype, type):
            ctype = type(ctype)
        if ctype not in cls._instance:
            self = cls._instance[ctype] = object.__new__(cls)
            self.__type = ctype
        return cls._instance[ctype]
    
    @cached_property
    def size(self):
        try:
            return ctypes.sizeof(self.__type)
        except TypeError:
            return 0
    
    @cached_property
    def type(self):
        return self.__type

    @cached_property
    def is_unsigned(self):
        return self.__type in c_type_category['unsigned'].values()
    
    @cached_property
    def is_signed(self):
        return self.__type in c_type_category['signed'].values() or issubclass(self.__type, int)
    
    @cached_property
    def is_float(self):
        return self.__type in c_type_category['float'].values() or issubclass(self.__type, float)

    def get_value(self, object):
        if self.size > 0 and hasattr(self.__type, 'value'):
            value_attr = self.__type.value
            if hasattr(value_attr, '__get__'):
                getter = value_attr.__get__
                if callable(getter):
                    return getter(object)
        return object

class CParser(pycparser.CParser):
    REGEXP_MULTILINE_COMMENT = re.compile(r'\/\*.*\*\/')
    REGEXP_SINGLELINE_COMMENT = re.compile(r'\/\/.*')
    REGEXP_FUNC_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)')
    REGEXP_VALUE_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\s+(.*)')

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
    def parse_c_string_literal(cls, value) -> str:
        first_quote_index = 0
        if value.startswith('u8'):
            first_quote_index = 2
        elif value.startswith('L') or value.startswith('U'):
            first_quote_index = 1
        if len(value) < 2 or value[first_quote_index] != '"' or value[-1] != '"':
            raise ValueError('Invalid string value (missing open or close quotes): %s' % value)
        return cls.parse_c_string(value[first_quote_index+1:-1])
    
    @classmethod
    def parse_c_string(cls, value) -> str:
        value = re.sub(r'\\U([0-9A-Fa-f]{8})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{1,3})', cls.subst_unicode_oct, value)
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
    }

    @classmethod
    def _preprocessor_get_lines(cls, code):
        lines = []
        code = cls.REGEXP_MULTILINE_COMMENT.sub('', code)
        code = code.splitlines()
        is_continuation_line = False
        for line in code:
            line = cls.REGEXP_SINGLELINE_COMMENT.sub('', line)
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

    @classmethod
    def parse_preprocessor(cls, code):
        code = cls._preprocessor_get_lines(code)
        if len(code) != 1:
            raise ValueError('Unable to define macro with more than one preprocessor line.')
        code = code[0]
        is_func_macro = cls.REGEXP_FUNC_MACRO.fullmatch(code)
        if is_func_macro is not None:
            return cls._parser_preprocessor_func(is_func_macro)
        is_value_macro = cls.REGEXP_VALUE_MACRO.fullmatch(code)
        if is_value_macro is not None:
            return cls._parser_preprocessor_value(is_value_macro)
    
    @classmethod
    def _parser_preprocessor_func(data: re.Match):
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
        return {
            'arguments': arguments,
            'template': template
        }
    
    @staticmethod
    def _parser_preprocessor_value(data: re.Match):
        return data.group(2)

def c_uchar_string_setter_check(value):
    if not isinstance(value, str):
        raise TypeError(f'unicode string expected instead of {value.__class__.__name__} instance')
    if len(value) != 1:
        raise TypeError('one character unicode string expected')

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

    subst_table = {v: k for k, v in CParser.subst_table.items()}

    @classmethod
    def generate_c_string(cls, value: str | bytes, *, encoding='utf-8'):
        if isinstance(value, str):
            value = value.encode(encoding=encoding)
        return '"' + re.sub(b'[\x00-\x1F\x7F-\xFF"\\]', cls._sub_string_escape, value) + '"'

    @staticmethod
    def _sub_string_escape(match):
        code = ord(match.group(0))
        if code in CParser.subst_string_table:
            return '\\' + CParser.subst_string_table[code]
        return '\\x%02x' % code

    @staticmethod
    def generate_c_int(value: int):
        return '%d' % value
    
    @staticmethod
    def generate_c_float(value: float, *, precision=10, suffix=''):
        if not math.isfinite():
            raise ValueError('C literals can only handle finite floating-point numbers')
        literal = '%.*g' % (precision, value)
        if '.' not in literal:
            literal += '.0'
        literal += suffix
        return literal
    
    @classmethod
    def generate_c_literal(cls, value, **kwargs):
        if isinstance(value, cls.Code):
            return value
        if isinstance(value, int):
            return cls.Code(cls.generate_c_int(value, **kwargs))
        if isinstance(value, float):
            return cls.Code(cls.generate_c_float(value, **kwargs))
        if isinstance(value, (str, bytes)):
            return cls.Code(cls.generate_c_string(value, **kwargs))
        raise TypeError('Unsupported C literal type: %s' % type(value).__qualname__)

class CContext:
    def __init__(self, *, types: Mapping = {}, values: Mapping = {}, definitions: Mapping = {}):
        self.types = types
        self.values = values
        self.definitions = definitions
        self.c_parser = CParser(self.types)
        self.c_generator = CGenerator()
    
    def c_preprocess_code_ast(self, code: str):
        ast = self.c_parser.parse(code)
        while self.c_preprocess_ast(ast):
            code = self.c_generator.visit(ast)
            ast = self.c_parser.parse(code)
        return ast
    
    def c_preprocess_ast(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.definitions and isinstance(self.definitions[child_node.name], str):
                setattr(node, name, self.c_generator.Code(self.definitions[child_node.name]))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.definitions and isinstance(self.definitions[child_node.name.name], dict):
                args = [self.c_generator.visit(x) for x in child_node.args]
                macro = self.definitions[child_node.name.name]
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
    
    def get_define_value(self, name):
        if name in self.definitions and isinstance(self.definitions[name], str):
            root = self.c_preprocess_code_ast(f'int var = {name};')
            return self.get_ast_expr_node_value(root.ext[0])

    @staticmethod
    def _create_ctype_buffer_from_string(value: str):
        return ctypes.create_string_buffer(value.encode())

    def _parse_string_literal_ctype(self, literal: str):
        start_index = 0
        method = self._create_ctype_buffer_from_string
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
    
    def get_ast_unary_operator(self, node: pycparser.c_ast.UnaryOp):
        arg = self.get_ast_expr_node_value(node.expr)
        arg_info = CTypeInfo(arg)
        arg_value = arg_info.get_value(arg)
        if isinstance(arg, (int, float, bool)):
            res_type = ctypes.c_bool if node.op in c_boolean_operators else arg_info.type
            res_value = c_value_operators['unary'][node.op](arg_value)
            return res_type(res_value)
        raise TypeError(f'Unary operation {node.op!r} not defined for argument of type {arg_info.type.__name__!r}')
    
    def get_ast_binary_operator(self, node: pycparser.c_ast.BinaryOp):
        left = self.get_ast_expr_node_value(node.left)
        right = self.get_ast_expr_node_value(node.right)
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

    def get_ast_expr_node_value(self, node: pycparser.c_ast.Node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if isinstance(node, c_ast.Constant):
            if 'int' in node.type:
                return c_native_types[node_type](self.c_parser.parse_c_int(node.value))
            elif node.type in ['float', 'double']:
                return c_native_types[node_type](self.c_parser.parse_c_float(node.value))
            elif node.type == 'string':
                return self._parse_string_literal_ctype(node.value)
        elif isinstance(node, c_ast.UnaryOp):
            return self.get_ast_unary_operator(node)
        elif isinstance(node, c_ast.BinaryOp):
            return self.get_ast_binary_operator(node)
        elif isinstance(node, c_ast.Cast):
            # Perform get_type_from_decl that recurse TypeDecl node.
            # Casting should be handled for at least c_native_type, pointers and arrays.
            # For array get_type_from_decl should use `get_ast_expr_node_value` to obtain a value for the length of the fixed array.
            raise NotImplementedError(f'Work-in-progress: {node.__name__!r} node')
        elif isinstance(node, c_ast.ID):
            # ID is searched in:
            # - context => named mapping on this function;
            # - self.values => named defitions for this context (can change during work);
            raise NotImplementedError(f'Work-in-progress: {node.__name__!r} node')