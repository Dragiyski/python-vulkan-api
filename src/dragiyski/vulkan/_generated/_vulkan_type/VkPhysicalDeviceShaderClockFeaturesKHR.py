import ctypes

class VkPhysicalDeviceShaderClockFeaturesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shaderSubgroupClock': ctypes.c_uint32,
            'shaderDeviceClock': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupClock', ctypes.c_uint32),
        ('shaderDeviceClock', ctypes.c_uint32),
    ]
