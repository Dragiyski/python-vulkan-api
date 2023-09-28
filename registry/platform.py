import ctypes as ctypes


class CType(dict):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._pointer = None

    def to_source(self, *args, **kwargs):
        raise NotImplementedError('This type cannot generate source')

    def to_python_type(self):
        raise NotImplementedError('This type has no corrensponding python type')

    def make_python_value(self, value):
        raise NotImplementedError('This type cannot convert python values')

    def pointer(self):
        return ctypes_map['c_void_p']

    def ctype():
        raise NotImplementedError('This type does not have "ctypes" representation')

    def __repr__(self):
        return '<CType>'


class CPlainType(CType):
    def __init__(self, ctype, **kwargs):
        super().__init__(**kwargs)
        if isinstance(ctype, str):
            if not hasattr(ctypes, ctype):
                raise ValueError('Cannot find "%s" type in ctypes' % ctype)
            obj = getattr(ctypes, ctype)
            try:
                ctypes.sizeof(obj)
            except TypeError:
                raise TypeError('The type "%s" is not valid ctype' % ctype)
        elif not isinstance(ctype, CType):
            raise TypeError('The type specified is not a string or ctype')
        self._ctype = ctype

    def to_source(self, *args, prefix='ctypes.', **kwargs):
        return '%s%s' % (prefix, self._ctype)

    def make_python_value(self, value):
        return getattr(ctypes, self._ctype)(value).value

    def ctype(self):
        return getattr(ctypes, self._ctype)

    def pointer(self):
        if self._pointer is None:
            self._pointer = CPointerType(self)
        return self._pointer

    def __repr__(self):
        return '<CType: %s>' % self._ctype


class CIntType(CPlainType):
    def to_python_type(self):
        return int


class CFloatType(CPlainType):
    def to_python_type(self):
        return float


class CPointerType(CIntType):
    def __init__(self, ctype, **kwargs):
        if not isinstance(ctype, CType):
            raise ValueError('Pointer type must be made from another CType')
        super().__init__(ctype, **kwargs)

    def to_source(self, *args, prefix='ctypes.', **kwargs):
        return '%s%s(%s)' % (prefix, 'POINTER', self._ctype.to_source(*args, prefix=prefix, **kwargs))

    def to_python_type(self):
        return int

    def make_python_value(self, value):
        return ctypes.c_void_p(value).value

    def __repr__(self):
        return "<CPointerType: %r>" % self._ctype


class CArrayType(CType):
    def __init__(self, ctype, length, **kwargs):
        if not isinstance(ctype, CType):
            raise ValueError('Pointer type must be made from another CType')
        if not isinstance(length, int):
            raise TypeError('CArrayType length must be an integer')
        super().__init__(**kwargs)
        self._ctype = ctype
        self._length = length

    def to_source(self, *args, prefix='ctypes.', **kwargs):
        return '%s%s(%s, %d)' % (prefix, 'ARRAY', self._ctype.to_source(*args, prefix=prefix, **kwargs), self._length)

    def pointer(self):
        if self._pointer is None:
            self._pointer = CPointerType(self)
        return self._pointer

    def __repr__(self):
        return "<CArrayType: %r[%d]>" % (self._ctype, self._length)


class CComplexType(CType):
    def __init__(self, name: str, constructor: str):
        if constructor not in ['Structure', 'Union']:
            raise ValueError('The constructor of complex type must be either "Structure" or "Union", got "%s"' % constructor)
        self._constructor = constructor
        self._name = name
        self.member_list = []
        self.member_map = {}
        self._pointer = None

    def to_source(self, **kwargs):
        return self._name

    def pointer(self):
        if self._pointer is None:
            self._pointer = CPointerType(self)
        return self._pointer

    def ctype(self):
        return getattr(ctypes, self._constructor)

    def append_field(self, name, ctype, **kwargs):
        assert name not in self.member_map
        assert name not in self.member_list
        self.member_list.append(name)
        self.member_map[name] = {
            'ctype': ctype,
            **kwargs
        }

    def __repr__(self):
        return "<CType %s(%s)>" % (self._constructor, self._name)


class CFunctionType(CType):
    def __init__(self, name: str):
        self._name = name
        self.constructor = 'ctypes.CFUNCTYPE'
        self.return_type = None
        self.argument_types = []
        self._pointer = None

    def to_source(self, **kwargs):
        return self._name

    def pointer(self):
        if self._pointer is None:
            self._pointer = CPointerType(self)
        return self._pointer

    def __repr__(self):
        return "<CType %s(%s)>" % ('Function', self._name)


class CBooleanType(CPlainType):
    def __init__(self):
        return super().__init__('c_bool')

    def to_python_type(self):
        return bool


class CStringType(CPlainType):
    def __init__(self):
        super().__init__('c_char_p')

    def to_python_type(self):
        return bytes


class CWideStringType(CPlainType):
    def __init__(self):
        super().__init__('c_wchar_p')

    def to_python_type(self):
        return str


class CCharType(CIntType):
    def __init__(self):
        super().__init__('c_char')

    def pointer(self):
        return ctypes_map['c_char_p']


class CWideCharType(CPlainType):
    def __init__(self):
        super().__init__('c_wchar')

    def to_python_type(self):
        return str

    def pointer(self):
        return ctypes_map['c_wchar_p']


# List of all known ctypes. All representable types must be in this dictionary or a complex type.
ctypes_map = {
    'void': CType(),
    'c_char': CCharType(),
    'c_wchar': CWideCharType(),
    'c_byte': CIntType('c_byte'),
    'c_ubyte': CIntType('c_ubyte'),
    'c_short': CIntType('c_short'),
    'c_ushort': CIntType('c_ushort'),
    'c_int': CIntType('c_int'),
    'c_uint': CIntType('c_uint'),
    'c_long': CIntType('c_long'),
    'c_ulong': CIntType('c_ulong'),
    'c_longlong': CIntType('c_longlong'),
    'c_ulonglong': CIntType('c_ulonglong'),
    'c_char_p': CStringType(),
    'c_bool': CBooleanType(),
    'c_size_t': CIntType('c_size_t'),
    'c_float': CFloatType('c_float'),
    'c_double': CFloatType('c_double'),
    'c_int8': CIntType('c_int8'),
    'c_uint8': CIntType('c_uint8'),
    'c_int16': CIntType('c_int16'),
    'c_uint16': CIntType('c_uint16'),
    'c_int32': CIntType('c_int32'),
    'c_uint32': CIntType('c_uint32'),
    'c_int64': CIntType('c_int64'),
    'c_uint64': CIntType('c_uint64'),
    'c_wchar_p': CWideStringType(),
    'c_void_p': CIntType('c_void_p')
}

# Representation of C types to specific object
basic_ctypes = {
    'void': ctypes_map['void'],
    'char': ctypes_map['c_char'],
    'float': ctypes_map['c_float'],
    'double': ctypes_map['c_double'],
    'int8_t': ctypes_map['c_int8'],
    'uint8_t': ctypes_map['c_uint8'],
    'int16_t': ctypes_map['c_int16'],
    'uint16_t': ctypes_map['c_uint16'],
    'uint32_t': ctypes_map['c_uint32'],
    'uint64_t': ctypes_map['c_uint64'],
    'int32_t': ctypes_map['c_int32'],
    'int64_t': ctypes_map['c_int64'],
    'size_t': ctypes_map['c_size_t'],
    'int': ctypes_map['c_int'],
    'bool': ctypes_map['c_bool'],
    'unsigned int': ctypes_map['c_uint'],
    'unsigned long': ctypes_map['c_ulong'],
    'unsigned long int': ctypes_map['c_ulong'],
    'unsigned short': ctypes_map['c_ushort'],
    'unsigned short int': ctypes_map['c_ushort'],
    'unsigned char': ctypes_map['c_ubyte'],
    'unsigned long long': ctypes_map['c_ulonglong'],
    'unsigned long long int': ctypes_map['c_ulonglong'],
    'int': ctypes_map['c_int'],
    'long': ctypes_map['c_long'],
    'long int': ctypes_map['c_long'],
    'short': ctypes_map['c_short'],
    'short int': ctypes_map['c_short'],
    'long long': ctypes_map['c_longlong'],
    'long long int': ctypes_map['c_longlong']
}

# Some plain types are coming from third party include files.
# Foreign types can be incomplete types (opaque), which used as pointer.
# However, some types are plain types used directly or known typedefs to a pointer.
platform_ctypes = {
    'VisualID': ctypes_map['c_uint32'],  # X11/Xlib.h: CARD32
    'Window': ctypes_map['c_uint32'],  # X11/Xlib.h: CARD32 => XID
    'RROutput': ctypes_map['c_uint32'],  # X11/extensions/Xrandr.h
    'xcb_window_t': ctypes_map['c_uint32'],  # xcb/xcb.h
    'xcb_visualid_t': ctypes_map['c_uint32'], # xcb/xcb.h
    'HINSTANCE': ctypes_map['c_void_p'],  # windows.h
    'HWND': ctypes_map['c_void_p'],  # windows.h
    'HMONITOR': ctypes_map['c_void_p'],  # windows.h
    'HANDLE': ctypes_map['c_void_p'],  # windows.h
    'DWORD': ctypes_map['c_uint32'],  # windows.h
    'LPCSTR': ctypes_map['c_char_p'],  # windows.h
    'LPCTSTR': ctypes_map['c_char_p'],  # windows.h
    'LPCWSTR': ctypes_map['c_wchar_p'],  # windows.h
    'zx_handle_t': ctypes_map['c_uint32'],  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': ctypes_map['c_uint32'],  # Google games platform?
    'GgpFrameToken': ctypes_map['c_uint32'],  # Google games platform?
    'NvSciSyncAttrList': ctypes_map['c_void_p'], # NV Sci Platform
    'NvSciSyncObj': ctypes_map['c_void_p'], # NV Sci Platform
    'NvSciSyncFence': CArrayType(ctypes_map['c_uint64'], 6), # NV Sci Platform
    'NvSciBufAttrList': ctypes_map['c_void_p'], # NV Sci Platform
    'NvSciBufObj': ctypes_map['c_void_p'], # NV Sci Platform
}

object_macro_map = {}
func_macro_map = {}
handle_type_map = {
    'VK_DEFINE_HANDLE': ctypes_map['c_void_p']
}

# vk.xml has preprocessor macros in <types>/<type category="define">
# Some of those are complex macros meant to run in a C preprocessor depending on:
# __x86_64__ which is identified by the C parser (python can detect that by ctypes.sizeof(ctypes.c_void_p))
# __cplusplus used to make very meaningful distinction of 0 as nullptr (in C++) or 0 as void * in C or 0 as unsigned long long for VK_NULL_HANDLE.
# In python 0 is 0 and c_void_p(0) will return None (NoneType instead of int)
# Hopefully, all other "define" types contains only simple #define (with potential comments)
if ctypes.sizeof(ctypes.c_void_p) == 8:
    object_macro_map['VK_USE_64_BIT_PTR_DEFINES'] = '(1)'
    object_macro_map['VK_NULL_HANDLE'] = '((void*)0)'
    handle_type_map['VK_DEFINE_NON_DISPATCHABLE_HANDLE'] = ctypes_map['c_void_p']
    func_macro_map['VK_DEFINE_NON_DISPATCHABLE_HANDLE'] = {
        'arguments': ['object'],
        'template': [
            'typedef struct ',
            {
                'name': 'object',
                'index': 0,
                'string': False
            },
            '_T* ',
            {
                'name': 'object',
                'index': 0,
                'string': False
            },
            ';'
        ]
    }
else:
    object_macro_map['VK_USE_64_BIT_PTR_DEFINES'] = '(0)'
    object_macro_map['VK_NULL_HANDLE'] = '(0ULL)'
    func_macro_map['VK_DEFINE_NON_DISPATCHABLE_HANDLE']
    handle_type_map['VK_DEFINE_NON_DISPATCHABLE_HANDLE'] = ctypes_map['c_uint64']
    macro_map['VK_DEFINE_NON_DISPATCHABLE_HANDLE'] = {
        'arguments': ['object'],
        'template': ['typedef uint64_t ', {'name': 'object', 'index': 0, 'string': False}, ';']
    }
