import ctypes

class VkCoarseSampleLocationNV(ctypes.Structure):
    _fields_ = [
        ('pixelX', ctypes.c_uint32),
        ('pixelY', ctypes.c_uint32),
        ('sample', ctypes.c_uint32),
    ]

VkCoarseSampleLocationNV._type_ = {
    'pixelX': ctypes.c_uint32,
    'pixelY': ctypes.c_uint32,
    'sample': ctypes.c_uint32,
}
