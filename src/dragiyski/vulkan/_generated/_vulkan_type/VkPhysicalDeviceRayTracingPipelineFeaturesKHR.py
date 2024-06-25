import ctypes

class VkPhysicalDeviceRayTracingPipelineFeaturesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'rayTracingPipeline': ctypes.c_uint32,
            'rayTracingPipelineShaderGroupHandleCaptureReplay': ctypes.c_uint32,
            'rayTracingPipelineShaderGroupHandleCaptureReplayMixed': ctypes.c_uint32,
            'rayTracingPipelineTraceRaysIndirect': ctypes.c_uint32,
            'rayTraversalPrimitiveCulling': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingPipeline', ctypes.c_uint32),
        ('rayTracingPipelineShaderGroupHandleCaptureReplay', ctypes.c_uint32),
        ('rayTracingPipelineShaderGroupHandleCaptureReplayMixed', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect', ctypes.c_uint32),
        ('rayTraversalPrimitiveCulling', ctypes.c_uint32),
    ]
