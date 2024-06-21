import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('flags', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('samples', ctypes.c_uint32),
        ('loadOp', ctypes.c_int),
        ('storeOp', ctypes.c_int),
        ('stencilLoadOp', ctypes.c_int),
        ('stencilStoreOp', ctypes.c_int),
        ('initialLayout', ctypes.c_int),
        ('finalLayout', ctypes.c_int),
    ]
