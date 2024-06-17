import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class StdVideoH264SliceType(VulkanIntEnum):
    STD_VIDEO_H264_SLICE_TYPE_B = 1
    STD_VIDEO_H264_SLICE_TYPE_I = 2
    STD_VIDEO_H264_SLICE_TYPE_INVALID = 2147483647
    STD_VIDEO_H264_SLICE_TYPE_P = 0

sys.modules[__name__] = StdVideoH264SliceType

