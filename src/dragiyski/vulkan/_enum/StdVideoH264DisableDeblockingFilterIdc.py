import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH264DisableDeblockingFilterIdc(VulkanIntEnum):
    STD_VIDEO_H264_DISABLE_DEBLOCKING_FILTER_IDC_DISABLED = 0
    STD_VIDEO_H264_DISABLE_DEBLOCKING_FILTER_IDC_ENABLED = 1
    STD_VIDEO_H264_DISABLE_DEBLOCKING_FILTER_IDC_INVALID = 2147483647
    STD_VIDEO_H264_DISABLE_DEBLOCKING_FILTER_IDC_PARTIAL = 2

sys.modules[__name__] = StdVideoH264DisableDeblockingFilterIdc

