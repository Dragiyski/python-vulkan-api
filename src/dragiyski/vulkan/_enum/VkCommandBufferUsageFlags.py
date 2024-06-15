import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkCommandBufferUsageFlags(VulkanUIntFlag):
    VK_COMMAND_BUFFER_USAGE_ONE_TIME_SUBMIT_BIT = 1
    VK_COMMAND_BUFFER_USAGE_RENDER_PASS_CONTINUE_BIT = 2
    VK_COMMAND_BUFFER_USAGE_SIMULTANEOUS_USE_BIT = 4

sys.modules[__name__] = VkCommandBufferUsageFlags

