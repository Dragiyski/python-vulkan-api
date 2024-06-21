import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]
