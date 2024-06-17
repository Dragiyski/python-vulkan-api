import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkQueryResultStatusKHR(VulkanIntEnum):
    VK_QUERY_RESULT_STATUS_COMPLETE_KHR = 1
    VK_QUERY_RESULT_STATUS_ERROR_KHR = -1
    VK_QUERY_RESULT_STATUS_INSUFFICIENT_BITSTREAM_BUFFER_RANGE_KHR = -1000299000
    VK_QUERY_RESULT_STATUS_NOT_READY_KHR = 0

sys.modules[__name__] = VkQueryResultStatusKHR

