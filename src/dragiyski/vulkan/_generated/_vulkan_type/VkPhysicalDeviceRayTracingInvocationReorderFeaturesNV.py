import ctypes

class VkPhysicalDeviceRayTracingInvocationReorderFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingInvocationReorder', ctypes.c_uint32),
    ]

VkPhysicalDeviceRayTracingInvocationReorderFeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingInvocationReorder': ctypes.c_uint32,
}
