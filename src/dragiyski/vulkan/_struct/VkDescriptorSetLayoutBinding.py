import ctypes, sys

class VkDescriptorSetLayoutBinding(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
        ('stageFlags', ctypes.c_uint32),
        ('pImmutableSamplers', ctypes.POINTER(ctypes.c_void_p)),
    ]

sys.modules[__name__] = VkDescriptorSetLayoutBinding
