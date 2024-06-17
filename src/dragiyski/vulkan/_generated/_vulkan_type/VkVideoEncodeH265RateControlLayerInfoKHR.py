import ctypes, sys

class VkVideoEncodeH265RateControlLayerInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265RateControlLayerInfoKHR

from . import VkVideoEncodeH265FrameSizeKHR
from . import VkVideoEncodeH265QpKHR

VkVideoEncodeH265RateControlLayerInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH265QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH265QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH265FrameSizeKHR),
]
