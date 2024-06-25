import ctypes

class VkMicromapBuildSizesInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('micromapSize', ctypes.c_uint64),
        ('buildScratchSize', ctypes.c_uint64),
        ('discardable', ctypes.c_uint32),
    ]

VkMicromapBuildSizesInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'micromapSize': ctypes.c_uint64,
    'buildScratchSize': ctypes.c_uint64,
    'discardable': ctypes.c_uint32,
}
