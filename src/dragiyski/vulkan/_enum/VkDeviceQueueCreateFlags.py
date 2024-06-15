import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDeviceQueueCreateFlags(VulkanUIntFlag):
    VK_DEVICE_QUEUE_CREATE_PROTECTED_BIT = 1

sys.modules[__name__] = VkDeviceQueueCreateFlags

