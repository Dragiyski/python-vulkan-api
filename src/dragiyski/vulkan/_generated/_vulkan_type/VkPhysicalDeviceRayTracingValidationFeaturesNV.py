import ctypes

class VkPhysicalDeviceRayTracingValidationFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingValidation', ctypes.c_uint32),
    ]

VkPhysicalDeviceRayTracingValidationFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingValidation': ctypes.c_uint32,
}
