import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class StdVideoAV1FrameType(VulkanIntEnum):
    STD_VIDEO_AV1_FRAME_TYPE_INTER = 1
    STD_VIDEO_AV1_FRAME_TYPE_INTRA_ONLY = 2
    STD_VIDEO_AV1_FRAME_TYPE_INVALID = 2147483647
    STD_VIDEO_AV1_FRAME_TYPE_KEY = 0
    STD_VIDEO_AV1_FRAME_TYPE_SWITCH = 3

sys.modules[__name__] = StdVideoAV1FrameType

