import ctypes

class VkRayTracingPipelineInterfaceCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxPipelineRayPayloadSize': ctypes.c_uint32,
            'maxPipelineRayHitAttributeSize': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPipelineRayPayloadSize', ctypes.c_uint32),
        ('maxPipelineRayHitAttributeSize', ctypes.c_uint32),
    ]
