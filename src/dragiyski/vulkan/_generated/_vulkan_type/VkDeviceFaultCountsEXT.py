import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('addressInfoCount', ctypes.c_uint32),
        ('vendorInfoCount', ctypes.c_uint32),
        ('vendorBinarySize', ctypes.c_uint64),
    ]
