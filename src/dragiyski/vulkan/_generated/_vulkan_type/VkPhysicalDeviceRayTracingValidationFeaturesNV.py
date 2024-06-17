import ctypes, sys

class VkPhysicalDeviceRayTracingValidationFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingValidation', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRayTracingValidationFeaturesNV
