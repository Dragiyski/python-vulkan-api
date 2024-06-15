import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkTimeDomainKHR(VulkanIntEnum):
    VK_TIME_DOMAIN_CLOCK_MONOTONIC_KHR = 1
    VK_TIME_DOMAIN_CLOCK_MONOTONIC_RAW_KHR = 2
    VK_TIME_DOMAIN_QUERY_PERFORMANCE_COUNTER_KHR = 3
    VK_TIME_DOMAIN_DEVICE_KHR = 0

sys.modules[__name__] = VkTimeDomainKHR
