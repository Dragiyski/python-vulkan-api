import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('value32', ctypes.c_uint32),
        ('value64', ctypes.c_uint64),
        ('valueFloat', ctypes.c_float),
        ('valueBool', ctypes.c_uint32),
        ('valueString', ctypes.c_char_p),
    ]
