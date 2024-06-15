import ctypes, sys

class VkVideoEncodeH264RateControlLayerInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264RateControlLayerInfoKHR

from . import VkVideoEncodeH264QpKHR
from . import VkVideoEncodeH264FrameSizeKHR

VkVideoEncodeH264RateControlLayerInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH264QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH264QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH264FrameSizeKHR),
]
