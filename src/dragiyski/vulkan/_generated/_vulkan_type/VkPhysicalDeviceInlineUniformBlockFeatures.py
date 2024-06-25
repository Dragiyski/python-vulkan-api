import ctypes

class VkPhysicalDeviceInlineUniformBlockFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('inlineUniformBlock', ctypes.c_uint32),
        ('descriptorBindingInlineUniformBlockUpdateAfterBind', ctypes.c_uint32),
    ]

VkPhysicalDeviceInlineUniformBlockFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'inlineUniformBlock': ctypes.c_uint32,
    'descriptorBindingInlineUniformBlockUpdateAfterBind': ctypes.c_uint32,
}
