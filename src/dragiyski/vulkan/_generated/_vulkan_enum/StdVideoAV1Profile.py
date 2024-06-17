import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class StdVideoAV1Profile(VulkanIntEnum):
    STD_VIDEO_AV1_PROFILE_HIGH = 1
    STD_VIDEO_AV1_PROFILE_INVALID = 2147483647
    STD_VIDEO_AV1_PROFILE_MAIN = 0
    STD_VIDEO_AV1_PROFILE_PROFESSIONAL = 2

sys.modules[__name__] = StdVideoAV1Profile

