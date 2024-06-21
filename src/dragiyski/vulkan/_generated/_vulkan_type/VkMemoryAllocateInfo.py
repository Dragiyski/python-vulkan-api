import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeIndex', ctypes.c_uint32),
    ]
