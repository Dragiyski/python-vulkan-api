import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sliceOffset', ctypes.c_uint32),
        ('sliceCount', ctypes.c_uint32),
    ]
