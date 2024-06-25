import ctypes

class VkDrmFormatModifierPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('drmFormatModifier', ctypes.c_uint64),
        ('drmFormatModifierPlaneCount', ctypes.c_uint32),
        ('drmFormatModifierTilingFeatures', ctypes.c_uint32),
    ]

VkDrmFormatModifierPropertiesEXT._type_ = {
    'drmFormatModifier': ctypes.c_uint64,
    'drmFormatModifierPlaneCount': ctypes.c_uint32,
    'drmFormatModifierTilingFeatures': ctypes.c_uint32,
}
