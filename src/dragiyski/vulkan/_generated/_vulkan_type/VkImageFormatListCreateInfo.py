import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('viewFormatCount', ctypes.c_uint32),
        ('pViewFormats', ctypes.POINTER(ctypes.c_int)),
    ]
