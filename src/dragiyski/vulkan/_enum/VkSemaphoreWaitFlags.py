import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSemaphoreWaitFlags(VulkanUIntFlag):
    VK_SEMAPHORE_WAIT_ANY_BIT = 1

sys.modules[__name__] = VkSemaphoreWaitFlags
