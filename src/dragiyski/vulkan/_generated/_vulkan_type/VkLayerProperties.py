import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('layerName', ctypes.ARRAY(ctypes.c_char, 256)),
        ('specVersion', ctypes.c_uint32),
        ('implementationVersion', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]
