import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkCommandBufferResetFlags(VulkanUIntFlag):
    VK_COMMAND_BUFFER_RESET_RELEASE_RESOURCES_BIT = 1

sys.modules[__name__] = VkCommandBufferResetFlags

