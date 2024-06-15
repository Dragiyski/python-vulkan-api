import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkResolveModeFlags(VulkanUIntFlag):
    VK_RESOLVE_MODE_AVERAGE_BIT = 2
    VK_RESOLVE_MODE_NONE = 0
    VK_RESOLVE_MODE_MIN_BIT = 4
    VK_RESOLVE_MODE_EXTERNAL_FORMAT_DOWNSAMPLE_ANDROID = 16
    VK_RESOLVE_MODE_SAMPLE_ZERO_BIT = 1
    VK_RESOLVE_MODE_MAX_BIT = 8

sys.modules[__name__] = VkResolveModeFlags
