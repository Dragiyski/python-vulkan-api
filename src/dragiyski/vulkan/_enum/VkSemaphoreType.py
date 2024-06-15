import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSemaphoreType(VulkanIntEnum):
    VK_SEMAPHORE_TYPE_TIMELINE = 1
    VK_SEMAPHORE_TYPE_BINARY = 0

sys.modules[__name__] = VkSemaphoreType
