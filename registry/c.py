import pycparser, re

# Maps all known C native types to ctypes (including some from stdint.h)
native_types = {
    'char': { 'class': 'ctypes', 'name': 'c_char' },
    'float': { 'class': 'ctypes', 'name': 'c_float' },
    'double': { 'class': 'ctypes', 'name': 'c_double' },
    'int8_t': { 'class': 'ctypes', 'name': 'c_int8' },
    'uint8_t': { 'class': 'ctypes', 'name': 'c_uint8' },
    'int16_t': { 'class': 'ctypes', 'name': 'c_int16' },
    'uint16_t': { 'class': 'ctypes', 'name': 'c_uint16' },
    'uint32_t': { 'class': 'ctypes', 'name': 'c_uint32' },
    'uint64_t': { 'class': 'ctypes', 'name': 'c_uint64' },
    'int32_t': { 'class': 'ctypes', 'name': 'c_int32' },
    'int64_t': { 'class': 'ctypes', 'name': 'c_int64' },
    'size_t': { 'class': 'ctypes', 'name': 'c_size_t' },
    'int': { 'class': 'ctypes', 'name': 'c_int' },
    'bool': { 'class': 'ctypes', 'name': 'c_bool' },
    'unsigned int': { 'class': 'ctypes', 'name': 'c_uint' },
    'unsigned long': { 'class': 'ctypes', 'name': 'c_ulong' },
    'unsigned long int': { 'class': 'ctypes', 'name': 'c_ulong' },
    'unsigned short': { 'class': 'ctypes', 'name': 'c_ushort' },
    'unsigned short int': { 'class': 'ctypes', 'name': 'c_ushort' },
    'unsigned char': { 'class': 'ctypes', 'name': 'c_ubyte' },
    'unsigned long long': { 'class': 'ctypes', 'name': 'c_ulonglong' },
    'unsigned long long int': { 'class': 'ctypes', 'name': 'c_ulonglong' },
    'int': { 'class': 'ctypes', 'name': 'c_int' },
    'long': { 'class': 'ctypes', 'name': 'c_long' },
    'long int': { 'class': 'ctypes', 'name': 'c_long' },
    'short': { 'class': 'ctypes', 'name': 'c_short' },
    'short int': { 'class': 'ctypes', 'name': 'c_short' },
    'long long': { 'class': 'ctypes', 'name': 'c_longlong' },
    'long long int': { 'class': 'ctypes', 'name': 'c_longlong' },
}

# Maps (hopefully) all external types that will be used by vulkan API
# Those cannot be found in the XML, only reference to appropriate header file is specified.
# Because C bindings are terrible, it means we had to hunt for those types in several APIs
# Luckily, the only conditional types seems to depend on the machine word size (i.e. pointer size),
# which means they will be bound to ctypes.c_void_p (even if they are not a pointer).
# ctypes.c_void_p is not derefencible in ctypes, it contains an int value, so it is okay
# to store machine word int, as long as we do not cast it to another pointer type.

# NOTE: If you are not on a platform that support certain of the APIs,
# those bindings will never be used as vkInstanceGetProcAddr and vkDeviceGetProcAddr won't
# return VK API that uses those types on unsuppoted platforms.
# However, properly processing the XML bindings would still require to know which types
# those types correspond. Unlike C, python bindings won't be implementation dependent on
# the choice of compiler, machine, cpu, arch, etc. A single piece of python code will run everywhere.
platform_types = {
    'VisualID': { 'class': 'ctypes', 'name': 'c_uint32' },  # X11/Xlib.h: CARD32
    'Window': { 'class': 'ctypes', 'name': 'c_uint32' },  # X11/Xlib.h: CARD32 => XID
    'RROutput': { 'class': 'ctypes', 'name': 'c_uint32' },  # X11/extensions/Xrandr.h
    'xcb_window_t': { 'class': 'ctypes', 'name': 'c_uint32' },  # xcb/xcb.h
    'xcb_visualid_t': { 'class': 'ctypes', 'name': 'c_uint32' }, # xcb/xcb.h
    'HINSTANCE': { 'class': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'HWND': { 'class': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'HMONITOR': { 'class': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'HANDLE': { 'class': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'DWORD': { 'class': 'ctypes', 'name': 'c_uint32' },  # windows.h
    'LPCSTR': { 'class': 'ctypes', 'name': 'c_char_p' },  # windows.h
    'LPCTSTR': { 'class': 'ctypes', 'name': 'c_char_p' },  # windows.h
    'LPCWSTR': { 'class': 'ctypes', 'name': 'c_wchar_p' },  # windows.h
    'zx_handle_t': { 'class': 'ctypes', 'name': 'c_uint32' },  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': { 'class': 'ctypes', 'name': 'c_uint32' },  # Google games platform?
    'GgpFrameToken': { 'class': 'ctypes', 'name': 'c_uint32' },  # Google games platform?
    'NvSciSyncAttrList': { 'class': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
    'NvSciSyncObj': { 'class': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
    'NvSciSyncFence': { 'class': 'array', 'type': { 'class': 'ctypes', 'name': 'c_uint64' }, 'length': 6 }, # NV Sci Platform
    'NvSciBufAttrList': { 'class': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
    'NvSciBufObj': { 'class': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
}

class CParser(pycparser.CParser):
    """
    Same as pycparser.CParser, but allow types to be specified in a python Container (usually Set)
    """
    def __init__(self, types = {}, **kwargs):
        super().__init__(**kwargs)
        self.c_types = set(types)

    def _lex_type_lookup_func(self, name):
        if super()._lex_type_lookup_func(name):
            return True
        return name in self.c_types
    
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
    def parse_c_string(cls, value):
        if len(value) < 2 or value[0] != '"' or value[-1] != '"':
            raise ValueError('Invalid string value (missing open or close quotes): %s' % value)
        value = value[1:-1]

        value = re.sub(r'\\U([0-9A-Fa-f]{8})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{3})', cls.subst_unicode_oct, value)
        value = re.sub(r'\\(.)', cls.subst_slash_escape, value)
        return value.encode('utf-8')

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