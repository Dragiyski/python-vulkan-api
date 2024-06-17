import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkSemaphoreWaitFlags(VulkanUIntFlag):
    VK_SEMAPHORE_WAIT_ANY_BIT = 1

sys.modules[__name__] = VkSemaphoreWaitFlags

VkSemaphoreWaitFlags.VK_SEMAPHORE_WAIT_ANY_BIT_KHR = VkSemaphoreWaitFlags.VK_SEMAPHORE_WAIT_ANY_BIT
