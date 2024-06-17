import ctypes, sys

class VkPhysicalDeviceInlineUniformBlockProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInlineUniformBlockSize', ctypes.c_uint32),
        ('maxPerStageDescriptorInlineUniformBlocks', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceInlineUniformBlockProperties
