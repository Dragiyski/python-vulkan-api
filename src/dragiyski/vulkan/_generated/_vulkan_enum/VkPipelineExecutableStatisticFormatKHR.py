import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkPipelineExecutableStatisticFormatKHR(VulkanIntEnum):
    VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_BOOL32_KHR = 0
    VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_FLOAT64_KHR = 3
    VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_INT64_KHR = 1
    VK_PIPELINE_EXECUTABLE_STATISTIC_FORMAT_UINT64_KHR = 2

sys.modules[__name__] = VkPipelineExecutableStatisticFormatKHR

