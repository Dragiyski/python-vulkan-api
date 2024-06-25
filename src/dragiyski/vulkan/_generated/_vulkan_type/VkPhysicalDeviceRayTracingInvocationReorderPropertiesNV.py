import ctypes

class VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingInvocationReorderReorderingHint', ctypes.c_int),
    ]

VkPhysicalDeviceRayTracingInvocationReorderPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingInvocationReorderReorderingHint': ctypes.c_int,
}
