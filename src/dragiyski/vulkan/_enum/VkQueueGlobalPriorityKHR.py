import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkQueueGlobalPriorityKHR(VulkanIntEnum):
    VK_QUEUE_GLOBAL_PRIORITY_LOW_KHR = 128
    VK_QUEUE_GLOBAL_PRIORITY_REALTIME_KHR = 1024
    VK_QUEUE_GLOBAL_PRIORITY_HIGH_KHR = 512
    VK_QUEUE_GLOBAL_PRIORITY_MEDIUM_KHR = 256

sys.modules[__name__] = VkQueueGlobalPriorityKHR
