import ctypes, sys

class VkPhysicalDeviceRayTracingPipelineFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingPipeline', ctypes.c_uint32),
        ('rayTracingPipelineShaderGroupHandleCaptureReplay', ctypes.c_uint32),
        ('rayTracingPipelineShaderGroupHandleCaptureReplayMixed', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect', ctypes.c_uint32),
        ('rayTraversalPrimitiveCulling', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRayTracingPipelineFeaturesKHR
