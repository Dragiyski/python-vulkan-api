import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfileIdc', ctypes.c_int),
        ('pictureLayout', ctypes.c_uint32),
    ]
