import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkFenceCreateFlags(VulkanUIntFlag):
    VK_FENCE_CREATE_SIGNALED_BIT = 1

sys.modules[__name__] = VkFenceCreateFlags

