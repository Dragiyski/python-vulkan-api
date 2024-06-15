import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoEncodeUsageFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_USAGE_CONFERENCING_BIT_KHR = 8
    VK_VIDEO_ENCODE_USAGE_DEFAULT_KHR = 0
    VK_VIDEO_ENCODE_USAGE_RECORDING_BIT_KHR = 4
    VK_VIDEO_ENCODE_USAGE_STREAMING_BIT_KHR = 2
    VK_VIDEO_ENCODE_USAGE_TRANSCODING_BIT_KHR = 1

sys.modules[__name__] = VkVideoEncodeUsageFlagsKHR

