import ctypes, sys

class VkDescriptorUpdateTemplateEntry(ctypes.Structure):
    _fields_ = [
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('offset', ctypes.c_size_t),
        ('stride', ctypes.c_size_t),
    ]

sys.modules[__name__] = VkDescriptorUpdateTemplateEntry
