import ctypes, sys

class VkDescriptorPoolInlineUniformBlockCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInlineUniformBlockBindings', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDescriptorPoolInlineUniformBlockCreateInfo
