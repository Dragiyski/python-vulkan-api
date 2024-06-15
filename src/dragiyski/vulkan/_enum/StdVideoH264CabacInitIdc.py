import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH264CabacInitIdc(VulkanIntEnum):
    STD_VIDEO_H264_CABAC_INIT_IDC_0 = 0
    STD_VIDEO_H264_CABAC_INIT_IDC_1 = 1
    STD_VIDEO_H264_CABAC_INIT_IDC_2 = 2
    STD_VIDEO_H264_CABAC_INIT_IDC_INVALID = 2147483647

sys.modules[__name__] = StdVideoH264CabacInitIdc
