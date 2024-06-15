import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSharingMode(VulkanIntEnum):
    VK_SHARING_MODE_CONCURRENT = 1
    VK_SHARING_MODE_EXCLUSIVE = 0

sys.modules[__name__] = VkSharingMode

