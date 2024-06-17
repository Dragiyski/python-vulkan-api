import ctypes, sys

class VkVideoEncodeRateControlLayerInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('averageBitrate', ctypes.c_uint64),
        ('maxBitrate', ctypes.c_uint64),
        ('frameRateNumerator', ctypes.c_uint32),
        ('frameRateDenominator', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeRateControlLayerInfoKHR
