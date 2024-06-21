import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH265QpKHR import CType as VkVideoEncodeH265QpKHR

CType._fields_ = [
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
