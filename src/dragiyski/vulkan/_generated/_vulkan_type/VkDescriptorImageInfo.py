import ctypes, sys

class VkDescriptorImageInfo(ctypes.Structure):
    _fields_ = [
        ('sampler', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]

sys.modules[__name__] = VkDescriptorImageInfo
