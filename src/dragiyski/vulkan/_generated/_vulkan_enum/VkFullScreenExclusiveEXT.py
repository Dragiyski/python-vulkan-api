import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkFullScreenExclusiveEXT(VulkanIntEnum):
    VK_FULL_SCREEN_EXCLUSIVE_ALLOWED_EXT = 1
    VK_FULL_SCREEN_EXCLUSIVE_APPLICATION_CONTROLLED_EXT = 3
    VK_FULL_SCREEN_EXCLUSIVE_DEFAULT_EXT = 0
    VK_FULL_SCREEN_EXCLUSIVE_DISALLOWED_EXT = 2

sys.modules[__name__] = VkFullScreenExclusiveEXT

