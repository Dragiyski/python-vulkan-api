import ctypes

class VkPhysicalDeviceLegacyDitheringFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('legacyDithering', ctypes.c_uint32),
    ]

VkPhysicalDeviceLegacyDitheringFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'legacyDithering': ctypes.c_uint32,
}
