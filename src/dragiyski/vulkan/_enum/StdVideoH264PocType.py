import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH264PocType(VulkanIntEnum):
    STD_VIDEO_H264_POC_TYPE_0 = 0
    STD_VIDEO_H264_POC_TYPE_1 = 1
    STD_VIDEO_H264_POC_TYPE_2 = 2
    STD_VIDEO_H264_POC_TYPE_INVALID = 2147483647

sys.modules[__name__] = StdVideoH264PocType

