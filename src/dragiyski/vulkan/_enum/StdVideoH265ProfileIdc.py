import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH265ProfileIdc(VulkanIntEnum):
    STD_VIDEO_H265_PROFILE_IDC_MAIN = 1
    STD_VIDEO_H265_PROFILE_IDC_INVALID = 2147483647
    STD_VIDEO_H265_PROFILE_IDC_FORMAT_RANGE_EXTENSIONS = 4
    STD_VIDEO_H265_PROFILE_IDC_MAIN_10 = 2
    STD_VIDEO_H265_PROFILE_IDC_MAIN_STILL_PICTURE = 3
    STD_VIDEO_H265_PROFILE_IDC_SCC_EXTENSIONS = 9

sys.modules[__name__] = StdVideoH265ProfileIdc
