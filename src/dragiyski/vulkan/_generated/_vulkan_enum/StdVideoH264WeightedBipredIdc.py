import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class StdVideoH264WeightedBipredIdc(VulkanIntEnum):
    STD_VIDEO_H264_WEIGHTED_BIPRED_IDC_DEFAULT = 0
    STD_VIDEO_H264_WEIGHTED_BIPRED_IDC_EXPLICIT = 1
    STD_VIDEO_H264_WEIGHTED_BIPRED_IDC_IMPLICIT = 2
    STD_VIDEO_H264_WEIGHTED_BIPRED_IDC_INVALID = 2147483647

sys.modules[__name__] = StdVideoH264WeightedBipredIdc

