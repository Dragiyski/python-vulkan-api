import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH265LevelIdc(VulkanIntEnum):
    STD_VIDEO_H265_LEVEL_IDC_1_0 = 0
    STD_VIDEO_H265_LEVEL_IDC_2_0 = 1
    STD_VIDEO_H265_LEVEL_IDC_2_1 = 2
    STD_VIDEO_H265_LEVEL_IDC_3_0 = 3
    STD_VIDEO_H265_LEVEL_IDC_3_1 = 4
    STD_VIDEO_H265_LEVEL_IDC_4_0 = 5
    STD_VIDEO_H265_LEVEL_IDC_4_1 = 6
    STD_VIDEO_H265_LEVEL_IDC_5_0 = 7
    STD_VIDEO_H265_LEVEL_IDC_5_1 = 8
    STD_VIDEO_H265_LEVEL_IDC_5_2 = 9
    STD_VIDEO_H265_LEVEL_IDC_6_0 = 10
    STD_VIDEO_H265_LEVEL_IDC_6_1 = 11
    STD_VIDEO_H265_LEVEL_IDC_6_2 = 12
    STD_VIDEO_H265_LEVEL_IDC_INVALID = 2147483647

sys.modules[__name__] = StdVideoH265LevelIdc

