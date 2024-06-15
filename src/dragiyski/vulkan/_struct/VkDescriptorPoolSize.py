import ctypes, sys

class VkDescriptorPoolSize(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDescriptorPoolSize
