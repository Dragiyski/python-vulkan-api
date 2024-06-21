import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('extensionName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
    ]
