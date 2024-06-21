import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInstances', ctypes.c_uint32),
        ('flags', ctypes.c_uint32),
    ]
