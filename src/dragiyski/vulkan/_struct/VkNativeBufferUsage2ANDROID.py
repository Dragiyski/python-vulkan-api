import ctypes, sys

class VkNativeBufferUsage2ANDROID(ctypes.Structure):
    _fields_ = [
        ('consumer', ctypes.c_uint64),
        ('producer', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkNativeBufferUsage2ANDROID
