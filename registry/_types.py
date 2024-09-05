class CType:
    def get_source(self):
        raise TypeError(f'Call of abstract method "CType.get_source".')

    def get_return_source(self):
        return self.get_source()


class CVoidType(CType):
    __singleton = None

    def __new__(cls):
        if cls.__singleton is None:
            cls.__singleton = object.__new__(cls)
        return cls.__singleton

    def get_source(self):
        raise TypeError(
            f'"{self.name}" is an external opaque type and cannot be used directly. Use a pointer instead.')

    def get_return_source(self):
        return 'None'
    
    @staticmethod
    def __repr__():
        return '<CVoidType>'


class CExternalType(CType):
    __name_map = {}

    def __new__(cls, name: str):
        if name not in cls.__name_map:
            cls.__name_map[name] = object.__new__(cls)
        return cls.__name_map[name]

    def __init__(self, name: str):
        self.name = name

    def get_source(self):
        raise TypeError(
            f'"{self.name}" is an external opaque type and cannot be used directly. Use a pointer instead.')

    def __repr__(self):
        return f'<CExternalType: {self.name}>'


class CCTypesType(CType):
    __ctypes_map = {}

    def __new__(cls, attribute: str):
        import ctypes
        if not hasattr(ctypes, attribute):
            raise TypeError(f'"{attribute}" is not a ctypes.<type>')
        ctype_class = getattr(ctypes, attribute)
        if not isinstance(ctype_class, type):
            raise TypeError(f'"{attribute}" is not a ctypes.<type>')
        try:
            ctypes.sizeof(ctype_class)
        except TypeError:
            raise TypeError(f'"{attribute}" is not a ctypes.<type>')
        if ctype_class not in cls.__ctypes_map:
            self = cls.__ctypes_map[ctype_class] = object.__new__(cls)
            self.__ctype_class = ctype_class
        return cls.__ctypes_map[ctype_class]

    def __init__(self, attribute):
        self.__attribute = attribute

    def get_source(self):
        return f'ctypes.{self.__ctypes_class.__name__}'

    def __repr__(self):
        return f'<CCTypesType: {self.__ctypes_class.__name__}>'


class CVulkanType(CType):
    pass


class ForeignType:
    def __init__(self, name: str):
        self.name = name


class PointerType:
    def __init__(self, ctype):
        self.ctype = ctype
