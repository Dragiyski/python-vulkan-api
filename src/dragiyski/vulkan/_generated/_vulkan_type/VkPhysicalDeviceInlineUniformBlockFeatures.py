import ctypes, sys

class VkPhysicalDeviceInlineUniformBlockFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceInlineUniformBlockFeatures
