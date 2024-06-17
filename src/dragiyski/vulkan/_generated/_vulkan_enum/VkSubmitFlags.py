import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkSubmitFlags(VulkanUIntFlag):
    VK_SUBMIT_PROTECTED_BIT = 1

sys.modules[__name__] = VkSubmitFlags

VkSubmitFlags.VK_SUBMIT_PROTECTED_BIT_KHR = VkSubmitFlags.VK_SUBMIT_PROTECTED_BIT
