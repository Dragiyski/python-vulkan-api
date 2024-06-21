import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcSubpass', ctypes.c_uint32),
        ('dstSubpass', ctypes.c_uint32),
        ('srcStageMask', ctypes.c_uint32),
        ('dstStageMask', ctypes.c_uint32),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
        ('dependencyFlags', ctypes.c_uint32),
    ]
