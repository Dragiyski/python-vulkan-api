import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoComponentBitDepthFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_COMPONENT_BIT_DEPTH_10_BIT_KHR = 4
    VK_VIDEO_COMPONENT_BIT_DEPTH_12_BIT_KHR = 16
    VK_VIDEO_COMPONENT_BIT_DEPTH_8_BIT_KHR = 1
    VK_VIDEO_COMPONENT_BIT_DEPTH_INVALID_KHR = 0

sys.modules[__name__] = VkVideoComponentBitDepthFlagsKHR

