import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPerformanceValueTypeINTEL(VulkanIntEnum):
    VK_PERFORMANCE_VALUE_TYPE_BOOL_INTEL = 3
    VK_PERFORMANCE_VALUE_TYPE_FLOAT_INTEL = 2
    VK_PERFORMANCE_VALUE_TYPE_STRING_INTEL = 4
    VK_PERFORMANCE_VALUE_TYPE_UINT32_INTEL = 0
    VK_PERFORMANCE_VALUE_TYPE_UINT64_INTEL = 1

sys.modules[__name__] = VkPerformanceValueTypeINTEL

