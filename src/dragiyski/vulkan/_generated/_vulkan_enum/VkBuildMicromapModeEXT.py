import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkBuildMicromapModeEXT(VulkanIntEnum):
    VK_BUILD_MICROMAP_MODE_BUILD_EXT = 0

sys.modules[__name__] = VkBuildMicromapModeEXT

