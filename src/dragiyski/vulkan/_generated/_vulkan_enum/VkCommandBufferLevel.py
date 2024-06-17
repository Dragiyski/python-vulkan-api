import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkCommandBufferLevel(VulkanIntEnum):
    VK_COMMAND_BUFFER_LEVEL_PRIMARY = 0
    VK_COMMAND_BUFFER_LEVEL_SECONDARY = 1

sys.modules[__name__] = VkCommandBufferLevel

