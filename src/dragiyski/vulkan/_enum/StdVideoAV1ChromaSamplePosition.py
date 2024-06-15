import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoAV1ChromaSamplePosition(VulkanIntEnum):
    STD_VIDEO_AV1_CHROMA_SAMPLE_POSITION_COLOCATED = 2
    STD_VIDEO_AV1_CHROMA_SAMPLE_POSITION_RESERVED = 3
    STD_VIDEO_AV1_CHROMA_SAMPLE_POSITION_INVALID = 2147483647
    STD_VIDEO_AV1_CHROMA_SAMPLE_POSITION_VERTICAL = 1
    STD_VIDEO_AV1_CHROMA_SAMPLE_POSITION_UNKNOWN = 0

sys.modules[__name__] = StdVideoAV1ChromaSamplePosition
