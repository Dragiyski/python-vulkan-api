import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('poolEntrySize', ctypes.c_uint64),
        ('poolEntryCount', ctypes.c_uint32),
    ]
