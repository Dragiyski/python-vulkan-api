import re, math, ctypes, operator, pycparser.c_ast, pycparser.c_generator
from collections.abc import Mapping
from collections import OrderedDict
from functools import cached_property

c_native_types = {
    'void': None,
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
        '!=': operator.ne,
        '<': operator.lt,
        '<=': operator.le,
        '>': operator.gt,
        '>=': operator.ge,
        '<<': operator.lshift,
        '>>': operator.rshift
    }
}

c_boolean_operators = { '!', '&&', '||', '==', '!=', '<', '>', '<=', '>=' }

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
            return -1
    
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
    
    @cached_property
    def _getter(self):
        if self.size > 0 and hasattr(self.__type, 'value'):
            value_attr = self.__type.value
            if hasattr(value_attr, '__get__'):
                getter = value_attr.__get__
                if callable(getter):
                    return getter
        return None

    def get_value(self, object):
        if callable(self._getter):
            return self._getter(object)
        return object

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
    
    @staticmethod
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
        value = re.sub(b'[\x00-\x1F\x7F-\xFF"\\\\]', cls._sub_string_escape, value).decode()
        return f'"{value}"'

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
