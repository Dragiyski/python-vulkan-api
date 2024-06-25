import ctypes

class VkImageDrmFormatModifierPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifier', ctypes.c_uint64),
    ]

VkImageDrmFormatModifierPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifier': ctypes.c_uint64,
}
