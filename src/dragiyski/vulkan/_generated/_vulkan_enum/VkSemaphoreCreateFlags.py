import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkSemaphoreCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkSemaphoreCreateFlags

