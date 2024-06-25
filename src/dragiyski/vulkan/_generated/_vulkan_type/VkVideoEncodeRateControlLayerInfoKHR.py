import ctypes

class VkVideoEncodeRateControlLayerInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'averageBitrate': ctypes.c_uint64,
            'maxBitrate': ctypes.c_uint64,
            'frameRateNumerator': ctypes.c_uint32,
            'frameRateDenominator': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('averageBitrate', ctypes.c_uint64),
        ('maxBitrate', ctypes.c_uint64),
        ('frameRateNumerator', ctypes.c_uint32),
        ('frameRateDenominator', ctypes.c_uint32),
    ]
