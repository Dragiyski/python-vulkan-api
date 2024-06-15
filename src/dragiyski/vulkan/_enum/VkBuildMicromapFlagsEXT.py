import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkBuildMicromapFlagsEXT(VulkanUIntFlag):
    VK_BUILD_MICROMAP_ALLOW_COMPACTION_BIT_EXT = 4
    VK_BUILD_MICROMAP_PREFER_FAST_BUILD_BIT_EXT = 2
    VK_BUILD_MICROMAP_PREFER_FAST_TRACE_BIT_EXT = 1

sys.modules[__name__] = VkBuildMicromapFlagsEXT

