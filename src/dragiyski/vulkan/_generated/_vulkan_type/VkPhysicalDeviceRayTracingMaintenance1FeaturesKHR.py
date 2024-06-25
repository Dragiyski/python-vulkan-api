import ctypes

class VkPhysicalDeviceRayTracingMaintenance1FeaturesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'rayTracingMaintenance1': ctypes.c_uint32,
            'rayTracingPipelineTraceRaysIndirect2': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingMaintenance1', ctypes.c_uint32),
        ('rayTracingPipelineTraceRaysIndirect2', ctypes.c_uint32),
    ]
