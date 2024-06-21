import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('aabbData', ctypes.c_void_p),
        ('numAABBs', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('offset', ctypes.c_uint64),
    ]
