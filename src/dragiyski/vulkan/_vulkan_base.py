import ctypes
from enum import IntEnum, IntFlag

class VulkanByteEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_byte(int(self))


class VulkanIntEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int(int(self))


class VulkanLongEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_long(int(self))


class VulkanShortEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_short(int(self))


class VulkanUByteEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_ubyte(int(self))


class VulkanUIntEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint(int(self))


class VulkanULongEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_ulong(int(self))


class VulkanUShortEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_ushort(int(self))


VulkanEnum = {
    ctypes.c_byte: VulkanByteEnum,
    ctypes.c_int: VulkanIntEnum,
    ctypes.c_long: VulkanLongEnum,
    ctypes.c_short: VulkanShortEnum,
    ctypes.c_ubyte: VulkanUByteEnum,
    ctypes.c_uint: VulkanUIntEnum,
    ctypes.c_ulong: VulkanULongEnum,
    ctypes.c_ushort: VulkanUShortEnum,
}

class VulkanByteFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_byte(int(self))


class VulkanIntFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int(int(self))


class VulkanLongFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_long(int(self))


class VulkanShortFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_short(int(self))


class VulkanUByteFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_ubyte(int(self))


class VulkanUIntFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint(int(self))


class VulkanULongFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_ulong(int(self))


class VulkanUShortFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_ushort(int(self))


VulkanFlag = {
    ctypes.c_byte: VulkanByteFlag,
    ctypes.c_int: VulkanIntFlag,
    ctypes.c_long: VulkanLongFlag,
    ctypes.c_short: VulkanShortFlag,
    ctypes.c_ubyte: VulkanUByteFlag,
    ctypes.c_uint: VulkanUIntFlag,
    ctypes.c_ulong: VulkanULongFlag,
    ctypes.c_ushort: VulkanUShortFlag,
}

class VulkanByte(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_byte(int(value))
        return value


class VulkanDouble(float):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_double(float(value))
        return value


class VulkanFloat(float):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_float(float(value))
        return value


class VulkanInt(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_int(int(value))
        return value


class VulkanLong(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_long(int(value))
        return value


class VulkanLongDouble(float):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_longdouble(float(value))
        return value


class VulkanShort(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_short(int(value))
        return value


class VulkanUByte(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_ubyte(int(value))
        return value


class VulkanUInt(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_uint(int(value))
        return value


class VulkanULong(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_ulong(int(value))
        return value


class VulkanUShort(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_ushort(int(value))
        return value


VulkanValue = {
    ctypes.c_byte: VulkanByte,
    ctypes.c_double: VulkanDouble,
    ctypes.c_float: VulkanFloat,
    ctypes.c_int: VulkanInt,
    ctypes.c_long: VulkanLong,
    ctypes.c_longdouble: VulkanLongDouble,
    ctypes.c_short: VulkanShort,
    ctypes.c_ubyte: VulkanUByte,
    ctypes.c_uint: VulkanUInt,
    ctypes.c_ulong: VulkanULong,
    ctypes.c_ushort: VulkanUShort,
}

if hasattr(ctypes, 'WINFUNCTYPE'):
    VKAPI_CALL = ctypes.WINFUNCTYPE
    VKAPI_PTR = ctypes.WINFUNCTYPE
else:
    VKAPI_CALL = ctypes.CFUNCTYPE
    VKAPI_PTR = ctypes.CFUNCTYPE

__all__ = [
    'VKAPI_CALL',
    'VKAPI_PTR',
    'VulkanByte',
    'VulkanByteEnum',
    'VulkanByteFlag',
    'VulkanDouble',
    'VulkanFloat',
    'VulkanInt',
    'VulkanIntEnum',
    'VulkanIntFlag',
    'VulkanLong',
    'VulkanLongDouble',
    'VulkanLongEnum',
    'VulkanLongFlag',
    'VulkanShort',
    'VulkanShortEnum',
    'VulkanShortFlag',
    'VulkanUByte',
    'VulkanUByteEnum',
    'VulkanUByteFlag',
    'VulkanUInt',
    'VulkanUIntEnum',
    'VulkanUIntFlag',
    'VulkanULong',
    'VulkanULongEnum',
    'VulkanULongFlag',
    'VulkanUShort',
    'VulkanUShortEnum',
    'VulkanUShortFlag',
]
