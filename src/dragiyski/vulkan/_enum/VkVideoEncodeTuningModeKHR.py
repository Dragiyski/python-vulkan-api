import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkVideoEncodeTuningModeKHR(VulkanIntEnum):
    VK_VIDEO_ENCODE_TUNING_MODE_DEFAULT_KHR = 0
    VK_VIDEO_ENCODE_TUNING_MODE_LOSSLESS_KHR = 4
    VK_VIDEO_ENCODE_TUNING_MODE_HIGH_QUALITY_KHR = 1
    VK_VIDEO_ENCODE_TUNING_MODE_ULTRA_LOW_LATENCY_KHR = 3
    VK_VIDEO_ENCODE_TUNING_MODE_LOW_LATENCY_KHR = 2

sys.modules[__name__] = VkVideoEncodeTuningModeKHR
