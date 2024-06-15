import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkQueryResultFlags(VulkanUIntFlag):
    VK_QUERY_RESULT_64_BIT = 1
    VK_QUERY_RESULT_WAIT_BIT = 2
    VK_QUERY_RESULT_WITH_STATUS_BIT_KHR = 16
    VK_QUERY_RESULT_PARTIAL_BIT = 8
    VK_QUERY_RESULT_WITH_AVAILABILITY_BIT = 4

sys.modules[__name__] = VkQueryResultFlags
