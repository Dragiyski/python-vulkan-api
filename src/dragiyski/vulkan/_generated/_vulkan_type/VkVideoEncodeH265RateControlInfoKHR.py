import ctypes

class VkVideoEncodeH265RateControlInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'gopFrameCount': ctypes.c_uint32,
            'idrPeriod': ctypes.c_uint32,
            'consecutiveBFrameCount': ctypes.c_uint32,
            'subLayerCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('gopFrameCount', ctypes.c_uint32),
        ('idrPeriod', ctypes.c_uint32),
        ('consecutiveBFrameCount', ctypes.c_uint32),
        ('subLayerCount', ctypes.c_uint32),
    ]
