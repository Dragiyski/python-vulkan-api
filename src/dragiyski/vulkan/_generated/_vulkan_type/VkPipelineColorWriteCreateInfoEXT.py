import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachmentCount', ctypes.c_uint32),
        ('pColorWriteEnables', ctypes.POINTER(ctypes.c_uint32)),
    ]
