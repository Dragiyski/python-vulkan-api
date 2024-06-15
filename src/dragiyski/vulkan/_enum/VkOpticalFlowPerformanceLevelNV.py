import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkOpticalFlowPerformanceLevelNV(VulkanIntEnum):
    VK_OPTICAL_FLOW_PERFORMANCE_LEVEL_MEDIUM_NV = 2
    VK_OPTICAL_FLOW_PERFORMANCE_LEVEL_UNKNOWN_NV = 0
    VK_OPTICAL_FLOW_PERFORMANCE_LEVEL_FAST_NV = 3
    VK_OPTICAL_FLOW_PERFORMANCE_LEVEL_SLOW_NV = 1

sys.modules[__name__] = VkOpticalFlowPerformanceLevelNV
