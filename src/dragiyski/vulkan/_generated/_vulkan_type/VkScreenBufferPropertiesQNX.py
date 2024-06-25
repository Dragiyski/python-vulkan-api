import ctypes

class VkScreenBufferPropertiesQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

VkScreenBufferPropertiesQNX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'allocationSize': ctypes.c_uint64,
    'memoryTypeBits': ctypes.c_uint32,
}
