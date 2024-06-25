import ctypes

class VkShaderModuleValidationCacheCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('validationCache', ctypes.c_void_p),
    ]

VkShaderModuleValidationCacheCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'validationCache': ctypes.c_void_p,
}
