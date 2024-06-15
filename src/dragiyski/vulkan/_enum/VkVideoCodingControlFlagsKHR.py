import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoCodingControlFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_CODING_CONTROL_ENCODE_QUALITY_LEVEL_BIT_KHR = 4
    VK_VIDEO_CODING_CONTROL_RESET_BIT_KHR = 1
    VK_VIDEO_CODING_CONTROL_ENCODE_RATE_CONTROL_BIT_KHR = 2

sys.modules[__name__] = VkVideoCodingControlFlagsKHR
