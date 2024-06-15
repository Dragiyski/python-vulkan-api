import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSemaphoreType(VulkanIntEnum):
    VK_SEMAPHORE_TYPE_BINARY = 0
    VK_SEMAPHORE_TYPE_TIMELINE = 1

sys.modules[__name__] = VkSemaphoreType

VkSemaphoreType.VK_SEMAPHORE_TYPE_BINARY_KHR = VkSemaphoreType.VK_SEMAPHORE_TYPE_BINARY
VkSemaphoreType.VK_SEMAPHORE_TYPE_TIMELINE_KHR = VkSemaphoreType.VK_SEMAPHORE_TYPE_TIMELINE
