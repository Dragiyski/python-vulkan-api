import ctypes

class VkNativeBufferUsage2ANDROID(ctypes.Structure):
    _fields_ = [
        ('consumer', ctypes.c_uint64),
        ('producer', ctypes.c_uint64),
    ]

VkNativeBufferUsage2ANDROID._type_ = {
    'consumer': ctypes.c_uint64,
    'producer': ctypes.c_uint64,
}
