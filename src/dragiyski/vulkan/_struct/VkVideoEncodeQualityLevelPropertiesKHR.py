import ctypes, sys

class VkVideoEncodeQualityLevelPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('preferredRateControlMode', ctypes.c_uint32),
        ('preferredRateControlLayerCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoEncodeQualityLevelPropertiesKHR
