import ctypes, sys

class VkVideoEncodeH264QualityLevelPropertiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264QualityLevelPropertiesKHR

from . import VkVideoEncodeH264QpKHR

VkVideoEncodeH264QualityLevelPropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('preferredRateControlFlags', ctypes.c_uint32),
    ('preferredGopFrameCount', ctypes.c_uint32),
    ('preferredIdrPeriod', ctypes.c_uint32),
    ('preferredConsecutiveBFrameCount', ctypes.c_uint32),
    ('preferredTemporalLayerCount', ctypes.c_uint32),
    ('preferredConstantQp', VkVideoEncodeH264QpKHR),
    ('preferredMaxL0ReferenceCount', ctypes.c_uint32),
    ('preferredMaxL1ReferenceCount', ctypes.c_uint32),
    ('preferredStdEntropyCodingModeFlag', ctypes.c_uint32),
]
