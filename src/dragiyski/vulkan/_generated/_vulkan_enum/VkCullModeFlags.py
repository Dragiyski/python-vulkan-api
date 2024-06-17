import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkCullModeFlags(VulkanUIntFlag):
    VK_CULL_MODE_BACK_BIT = 2
    VK_CULL_MODE_FRONT_AND_BACK = 3
    VK_CULL_MODE_FRONT_BIT = 1
    VK_CULL_MODE_NONE = 0

sys.modules[__name__] = VkCullModeFlags

