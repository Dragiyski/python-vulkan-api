import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkVideoDecodeUsageFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_DECODE_USAGE_DEFAULT_KHR = 0
    VK_VIDEO_DECODE_USAGE_OFFLINE_BIT_KHR = 2
    VK_VIDEO_DECODE_USAGE_STREAMING_BIT_KHR = 4
    VK_VIDEO_DECODE_USAGE_TRANSCODING_BIT_KHR = 1

sys.modules[__name__] = VkVideoDecodeUsageFlagsKHR

