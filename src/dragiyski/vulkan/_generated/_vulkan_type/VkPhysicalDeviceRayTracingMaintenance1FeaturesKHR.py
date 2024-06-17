import ctypes, sys

class VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMaintenance1', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect2', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR
