import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkCommandPoolResetFlags(VulkanUIntFlag):
    VK_COMMAND_POOL_RESET_RELEASE_RESOURCES_BIT = 1

sys.modules[__name__] = VkCommandPoolResetFlags
