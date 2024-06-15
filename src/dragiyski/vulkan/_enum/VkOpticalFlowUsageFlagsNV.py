import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkOpticalFlowUsageFlagsNV(VulkanUIntFlag):
    VK_OPTICAL_FLOW_USAGE_COST_BIT_NV = 8
    VK_OPTICAL_FLOW_USAGE_GLOBAL_FLOW_BIT_NV = 16
    VK_OPTICAL_FLOW_USAGE_HINT_BIT_NV = 4
    VK_OPTICAL_FLOW_USAGE_INPUT_BIT_NV = 1
    VK_OPTICAL_FLOW_USAGE_OUTPUT_BIT_NV = 2
    VK_OPTICAL_FLOW_USAGE_UNKNOWN_NV = 0

sys.modules[__name__] = VkOpticalFlowUsageFlagsNV

