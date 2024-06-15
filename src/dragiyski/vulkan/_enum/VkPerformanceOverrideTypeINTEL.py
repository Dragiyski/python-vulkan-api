import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPerformanceOverrideTypeINTEL(VulkanIntEnum):
    VK_PERFORMANCE_OVERRIDE_TYPE_FLUSH_GPU_CACHES_INTEL = 1
    VK_PERFORMANCE_OVERRIDE_TYPE_NULL_HARDWARE_INTEL = 0

sys.modules[__name__] = VkPerformanceOverrideTypeINTEL
