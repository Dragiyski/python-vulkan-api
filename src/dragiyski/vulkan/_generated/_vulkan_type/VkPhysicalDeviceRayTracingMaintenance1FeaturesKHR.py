import ctypes

class VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMaintenance1', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect2', ctypes.c_uint32),
    ]

VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'rayTracingMaintenance1': ctypes.c_uint32,
    'rayTracingPipelineTraceRaysIndirect2': ctypes.c_uint32,
}
