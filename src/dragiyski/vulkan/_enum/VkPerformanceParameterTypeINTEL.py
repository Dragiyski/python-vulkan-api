import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPerformanceParameterTypeINTEL(VulkanIntEnum):
    VK_PERFORMANCE_PARAMETER_TYPE_HW_COUNTERS_SUPPORTED_INTEL = 0
    VK_PERFORMANCE_PARAMETER_TYPE_STREAM_MARKER_VALID_BITS_INTEL = 1

sys.modules[__name__] = VkPerformanceParameterTypeINTEL

