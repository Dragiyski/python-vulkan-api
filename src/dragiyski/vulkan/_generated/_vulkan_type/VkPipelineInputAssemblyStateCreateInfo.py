import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('topology', ctypes.c_int),
        ('primitiveRestartEnable', ctypes.c_uint32),
    ]
