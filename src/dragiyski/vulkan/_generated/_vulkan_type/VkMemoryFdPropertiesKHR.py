import ctypes

class VkMemoryFdPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

VkMemoryFdPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryTypeBits': ctypes.c_uint32,
}
