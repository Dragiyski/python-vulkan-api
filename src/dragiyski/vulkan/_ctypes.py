import ctypes
import typing
import collections.abc
from collections import OrderedDict

if hasattr(ctypes, 'WINFUNCTYPE'):
    VKAPI_CALL = ctypes.WINFUNCTYPE
    VKAPI_PTR = ctypes.WINFUNCTYPE
else:
    VKAPI_CALL = ctypes.CFUNCTYPE
    VKAPI_PTR = ctypes.CFUNCTYPE

ctypes_map = {}
implementation_map = {}

class CType:
    def __new__(cls, *args, **kwargs):
        raise TypeError('Initialization of abstract type')
    
    def __init__(self, *args, **kwargs):
        pass

    def get_python_type(self):
        return None
    
    @staticmethod
    def append_hint_deps(deps: dict):
        pass
    
    @staticmethod
    def get_hint_source():
        return 'None'
    
    def __repr__(self):
        return '<%s>' % self.__class__.__name__
    
class CVoidType(CType):
    def __new__(cls):
        return ctypes_map['void']

    @staticmethod
    def get_c_type():
        return None
    
    @staticmethod
    def pointer():
        return ctypes_map['c_void_p']

class CPlainType(CType):
    __type_map = {}
    def __new__(cls, name):
        if name not in ctypes_map:
            ctype = getattr(ctypes, name, None)
            try:
                ctypes.sizeof(ctype)
            except TypeError:
                raise TypeError('Invalid simple type: ctypes.%s does not exists or it is not a type' % name)
            if ctype not in cls.__type_map:
                self = object.__new__(cls)
                cls._init(self, ctype)
                cls.__type_map[name] = self
        return cls.__type_map[name]
    
    def _init(self, ctype = None):
        self.__name = ctype.__name__
        self._ctype = ctype
    
    def pointer(self):
        return CPointerType(self)
    
    def get_c_type(self):
        return self._ctype
    
    @staticmethod
    def get_hint_source():
        raise ValueError('Abstract method: %s' % 'CPlainType.get_hint_source')
    
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.__name)

class CIntType(CPlainType):
    @staticmethod
    def get_python_type():
        return int
    
    @staticmethod
    def get_hint_type():
        return int
    
    @staticmethod
    def get_hint_source():
        return 'int'

class CFloatType(CPlainType):
    @staticmethod
    def get_python_type():
        return float
    
    @staticmethod
    def get_hint_type():
        return float
    
    @staticmethod
    def get_hint_source():
        return 'float'

class CPointerType(CIntType):
    __pointer_map = {}
    def __new__(cls, base_type):
        if base_type not in cls.__pointer_map:
            self = object.__new__(cls)
            cls._init(self, base_type)
            cls.__pointer_map[base_type] = self
        return cls.__pointer_map[base_type]
    
    def _init(self, base_type):
        self.type = base_type

    def append_hint_deps(self, deps: dict):
        if 'ctypes' not in deps:
            deps['ctypes'] = set()
        deps['ctypes'].add(False)
        self.type.append_hint_deps(deps)

    def get_hint_source(self):
        if self.type.__class__ in [CType, CVoidType]:
            return 'ctypes.c_void_p'
        return 'ctypes._Pointer[%s]' % self.type.get_hint_source()
    
    def __repr__(self):
        return '<%s: %r>' % (self.__class__.__name__, self.type)

class CArrayType(CType):
    __array_map = {}
    def __new__(cls, base_type, length):
        if base_type not in cls.__array_map:
            cls.__array_map[base_type] = {}
        if length not in cls.__array_map[base_type]:
            self = object.__new__(cls)
            cls._init(self, base_type, length)
            cls.__array_map[base_type][length] = self
        return cls.__array_map[base_type][length]
    
    def _init(self, base_type, length):
        self.type = base_type
        self.length = length
    
    def get_c_type(self):
        return self.type.get_c_type() * self.length
    
    def get_hint_type(self):
        return collections.abc.Collection[self.type.get_hint_type()]
    
    def append_hint_deps(self, deps: dict):
        if 'collections.abc' not in deps:
            deps['collections.abc'] = set()
        deps['collections.abc'].add('Collection')
        self.type.append_hint_deps(deps)

    def get_hint_source(self):
        types = ['Collection[%s]' % self.type.get_hint_source()]
        if isinstance(self.type, CPlainType):
            if self.type.get_c_type() == ctypes.c_char:
                types.append('bytes')
            elif self.type.get_c_type() == ctypes.c_wchar:
                types.append('str')
        return ' | '.join(types)
    
    def get_python_type(self):
        return list
    
    def __repr__(self):
        return '<%s: [%d] %r>' % (self.__class__.__name__, self.length, self.type)

class CComplexType(CType):
    __complex_map = {}
    def __new__(cls, name):
        if name not in cls.__complex_map:
            self = object.__new__(cls)
            cls._init(self, name)
            cls.__complex_map[name] = self
        return cls.__complex_map[name]
    
    def _init(self, name):
        self.name = name
        self.fields = OrderedDict()
    
    def get_python_type(self):
        return super().get_python_type()
    
    def get_c_type(self):
        return self._class_
    
    def get_hint_type(self):
        return self._class_
    
    def pointer(self):
        return CPointerType(self)
    
    def append_hint_deps(self, deps: dict):
        module = self._class_.__module__
        if module not in deps:
            deps[module] = set()
        deps[module].add(self._class_.__name__)
    
    def get_hint_source(self):
        return self.name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

class CFunctionType(CType):
    __function_map = {}
    def __new__(cls, name):
        if name not in cls.__function_map:
            self = object.__new__(cls)
            self.name = name
            cls.__function_map[name] = self
        return cls.__function_map[name]
    
    def __init__(self, name):
        self.name = name
        self.return_type = None
        self.arguments = OrderedDict()
    
    def pointer(self):
        return CPointerType(self)
    
    def get_c_type(self):
        return self._class_
    
    @staticmethod
    def append_hint_deps(deps: dict):
       pass
    
    def get_hint_source(self):
        return self.name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)

class CBooleanType(CPlainType):
    @staticmethod
    def get_hint_type():
        return bool
    
    @staticmethod
    def get_python_type():
        return bool
    
    @staticmethod
    def get_hint_source():
        return 'bool'
    
class CStringType(CPlainType):
    def __new__(cls, type):
        if type != 'c_char_p':
            raise TypeError('Invalid CStringType: %s' % type)
        return super().__new__(cls, type)

    @staticmethod
    def get_hint_type():
        return bytes | str
    
    @staticmethod
    def get_python_type():
        return bytes
    
    @staticmethod
    def get_hint_source():
        return 'bytes'

class CWideStringType(CPlainType):
    def __new__(cls, type):
        if type != 'c_wchar_p':
            raise TypeError('Invalid CWideStringType: %s' % type)
        return super().__new__(cls, type)

    def get_hint_type(self):
        return str

    def get_python_type(self):
        return str
    
    @staticmethod
    def get_hint_source():
        return 'str'

class CCharType(CIntType):
    def __new__(cls, type):
        if type != 'c_char':
            raise TypeError('Invalid CCharType: %s' % type)
        return super().__new__(cls, type)

    def pointer(self):
        return ctypes_map['c_char_p']

class CWideCharType(CPlainType):
    def __new__(cls, type):
        if type != 'c_wchar':
            raise TypeError('Invalid CWideCharType: %s' % type)
        return super().__new__(cls, type)

    def get_python_type(self):
        return str

    def get_hint_type(self):
        return str
    
    @staticmethod
    def get_hint_source():
        return 'str'

    def pointer(self):
        return ctypes_map['c_wchar_p']

class CHandleType(CIntType):
    __handle_map = {}
    def __new__(cls, name):
        if name not in cls.__handle_map:
            self = object.__new__(cls)
            # Note: Vulkan Headers set handles to 64-bit always (even on 32-bit system)
            # That is: void* on 64-bit or uint64_t on 32-bit.
            cls._init(self, ctypes_map['c_void_p' if ctypes.sizeof(ctypes.c_void_p) == 8 else 'c_uint64'].get_c_type())
            cls.__handle_map[name] = self
            self.name = name
        return cls.__handle_map[name]
    
    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)


ctypes_map.update({
    'void': object.__new__(CVoidType),
    'c_char': CCharType('c_char'),
    'c_wchar': CWideCharType('c_wchar'),
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
    'c_char_p': CStringType('c_char_p'),
    'c_bool': CBooleanType('c_bool'),
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
    'c_wchar_p': CWideStringType('c_wchar_p'),
    'c_void_p': CIntType('c_void_p')
})
