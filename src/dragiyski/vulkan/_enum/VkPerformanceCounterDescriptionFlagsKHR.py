import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPerformanceCounterDescriptionFlagsKHR(VulkanUIntFlag):
    VK_PERFORMANCE_COUNTER_DESCRIPTION_PERFORMANCE_IMPACTING_BIT_KHR = 1
    VK_PERFORMANCE_COUNTER_DESCRIPTION_CONCURRENTLY_IMPACTED_BIT_KHR = 2

sys.modules[__name__] = VkPerformanceCounterDescriptionFlagsKHR