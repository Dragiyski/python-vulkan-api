import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorOffset', ctypes.c_size_t),
        ('descriptorSize', ctypes.c_uint32),
    ]
