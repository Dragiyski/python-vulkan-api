import ctypes
from enum import IntEnum, IntFlag

class VulkanIntEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int(int(self))

class VulkanUIntEnum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint(int(self))

class VulkanUInt32Enum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint32(int(self))

class VulkanUInt64Enum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint64(int(self))

class VulkanInt32Enum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int32(int(self))

class VulkanInt64Enum(IntEnum):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int64(int(self))

VulkanEnum = {
    ctypes.c_int: VulkanIntEnum,
    ctypes.c_uint: VulkanUIntEnum,
    ctypes.c_int32: VulkanInt32Enum,
    ctypes.c_uint32: VulkanUInt32Enum,
    ctypes.c_int64: VulkanInt64Enum,
    ctypes.c_uint64: VulkanUInt64Enum,
}

class VulkanIntFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int(int(self))

class VulkanUIntFlag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint(int(self))

class VulkanUInt32Flag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint32(int(self))

class VulkanUInt64Flag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_uint64(int(self))

class VulkanInt32Flag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int32(int(self))

class VulkanInt64Flag(IntFlag):
    def __init__(self, *args, **kwargs):
        self._as_parameter_ = ctypes.c_int64(int(self))

VulkanFlag = {
    ctypes.c_int: VulkanIntFlag,
    ctypes.c_uint: VulkanUIntFlag,
    ctypes.c_int32: VulkanInt32Flag,
    ctypes.c_uint32: VulkanUInt32Flag,
    ctypes.c_int64: VulkanInt64Flag,
    ctypes.c_uint64: VulkanUInt64Flag,
}

class VulkanInt(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_int(int(value))
        return value

class VulkanUInt(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_uint(int(value))
        return value

class VulkanInt32(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_int32(int(value))
        return value

class VulkanUInt32(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_uint32(int(value))
        return value

class VulkanInt64(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_int64(int(value))
        return value

class VulkanUInt64(int):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_uint64(int(value))
        return value

class VulkanFloat(float):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_float(float(value))
        return value

class VulkanDouble(float):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_double(float(value))
        return value

class VulkanLongDouble(float):
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        value._as_parameter_ = ctypes.c_longdouble(float(value))
        return value
        
VulkanConst = {
    ctypes.c_int: VulkanInt,
    ctypes.c_uint: VulkanUInt,
    ctypes.c_int32: VulkanInt32,
    ctypes.c_uint32: VulkanUInt32,
    ctypes.c_int64: VulkanInt64,
    ctypes.c_uint64: VulkanUInt64,
    ctypes.c_float: VulkanFloat,
    ctypes.c_double: VulkanDouble,
    ctypes.c_longdouble: VulkanLongDouble
}
