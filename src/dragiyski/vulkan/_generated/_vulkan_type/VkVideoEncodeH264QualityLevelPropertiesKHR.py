import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH264QpKHR import CType as VkVideoEncodeH264QpKHR

CType._fields_ = [
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
