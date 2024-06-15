import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDiscardRectangleModeEXT(VulkanIntEnum):
    VK_DISCARD_RECTANGLE_MODE_EXCLUSIVE_EXT = 1
    VK_DISCARD_RECTANGLE_MODE_INCLUSIVE_EXT = 0

sys.modules[__name__] = VkDiscardRectangleModeEXT

