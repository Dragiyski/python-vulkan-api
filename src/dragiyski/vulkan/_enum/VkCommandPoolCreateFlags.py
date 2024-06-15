import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkCommandPoolCreateFlags(VulkanUIntFlag):
    VK_COMMAND_POOL_CREATE_PROTECTED_BIT = 4
    VK_COMMAND_POOL_CREATE_RESET_COMMAND_BUFFER_BIT = 2
    VK_COMMAND_POOL_CREATE_TRANSIENT_BIT = 1

sys.modules[__name__] = VkCommandPoolCreateFlags
