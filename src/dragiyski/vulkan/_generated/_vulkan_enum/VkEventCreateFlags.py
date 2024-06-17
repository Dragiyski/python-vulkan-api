import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkEventCreateFlags(VulkanUIntFlag):
    VK_EVENT_CREATE_DEVICE_ONLY_BIT = 1

sys.modules[__name__] = VkEventCreateFlags

VkEventCreateFlags.VK_EVENT_CREATE_DEVICE_ONLY_BIT_KHR = VkEventCreateFlags.VK_EVENT_CREATE_DEVICE_ONLY_BIT
