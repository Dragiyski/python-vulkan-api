import ctypes, sys

class VkShaderModuleValidationCacheCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('validationCache', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkShaderModuleValidationCacheCreateInfoEXT
