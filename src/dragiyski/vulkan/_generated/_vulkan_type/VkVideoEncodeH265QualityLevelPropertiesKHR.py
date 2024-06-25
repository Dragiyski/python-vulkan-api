import ctypes

class VkVideoEncodeH265QualityLevelPropertiesKHR(ctypes.Structure):
    pass

from .VkVideoEncodeH265QpKHR import VkVideoEncodeH265QpKHR

VkVideoEncodeH265QualityLevelPropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('preferredRateControlFlags', ctypes.c_uint32),
    ('preferredGopFrameCount', ctypes.c_uint32),
    ('preferredIdrPeriod', ctypes.c_uint32),
    ('preferredConsecutiveBFrameCount', ctypes.c_uint32),
    ('preferredSubLayerCount', ctypes.c_uint32),
    ('preferredConstantQp', VkVideoEncodeH265QpKHR),
    ('preferredMaxL0ReferenceCount', ctypes.c_uint32),
    ('preferredMaxL1ReferenceCount', ctypes.c_uint32),
]

VkVideoEncodeH265QualityLevelPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'preferredRateControlFlags': ctypes.c_uint32,
    'preferredGopFrameCount': ctypes.c_uint32,
    'preferredIdrPeriod': ctypes.c_uint32,
    'preferredConsecutiveBFrameCount': ctypes.c_uint32,
    'preferredSubLayerCount': ctypes.c_uint32,
    'preferredConstantQp': VkVideoEncodeH265QpKHR,
    'preferredMaxL0ReferenceCount': ctypes.c_uint32,
    'preferredMaxL1ReferenceCount': ctypes.c_uint32,
}
