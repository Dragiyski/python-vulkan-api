import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stages', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('subgroupSize', ctypes.c_uint32),
    ]
