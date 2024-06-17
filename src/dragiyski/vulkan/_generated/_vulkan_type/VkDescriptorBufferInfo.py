import ctypes, sys

class VkDescriptorBufferInfo(ctypes.Structure):
    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkDescriptorBufferInfo
