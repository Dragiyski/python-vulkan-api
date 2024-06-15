import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoDecodeH264FieldOrderCount(VulkanIntEnum):
    STD_VIDEO_DECODE_H264_FIELD_ORDER_COUNT_BOTTOM = 1
    STD_VIDEO_DECODE_H264_FIELD_ORDER_COUNT_INVALID = 2147483647
    STD_VIDEO_DECODE_H264_FIELD_ORDER_COUNT_TOP = 0

sys.modules[__name__] = StdVideoDecodeH264FieldOrderCount

