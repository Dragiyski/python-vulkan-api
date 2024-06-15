import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH264ProfileIdc(VulkanIntEnum):
    STD_VIDEO_H264_PROFILE_IDC_BASELINE = 66
    STD_VIDEO_H264_PROFILE_IDC_HIGH = 100
    STD_VIDEO_H264_PROFILE_IDC_HIGH_444_PREDICTIVE = 244
    STD_VIDEO_H264_PROFILE_IDC_INVALID = 2147483647
    STD_VIDEO_H264_PROFILE_IDC_MAIN = 77

sys.modules[__name__] = StdVideoH264ProfileIdc

