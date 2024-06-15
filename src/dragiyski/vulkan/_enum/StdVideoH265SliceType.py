import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH265SliceType(VulkanIntEnum):
    STD_VIDEO_H265_SLICE_TYPE_INVALID = 2147483647
    STD_VIDEO_H265_SLICE_TYPE_B = 0
    STD_VIDEO_H265_SLICE_TYPE_P = 1
    STD_VIDEO_H265_SLICE_TYPE_I = 2

sys.modules[__name__] = StdVideoH265SliceType
