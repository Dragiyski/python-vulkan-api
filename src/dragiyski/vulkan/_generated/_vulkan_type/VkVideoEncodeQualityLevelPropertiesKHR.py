import ctypes

class VkVideoEncodeQualityLevelPropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'preferredRateControlMode': ctypes.c_uint32,
            'preferredRateControlLayerCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('preferredRateControlMode', ctypes.c_uint32),
        ('preferredRateControlLayerCount', ctypes.c_uint32),
    ]
