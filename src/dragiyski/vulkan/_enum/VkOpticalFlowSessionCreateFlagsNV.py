import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkOpticalFlowSessionCreateFlagsNV(VulkanUIntFlag):
    VK_OPTICAL_FLOW_SESSION_CREATE_ALLOW_REGIONS_BIT_NV = 8
    VK_OPTICAL_FLOW_SESSION_CREATE_BOTH_DIRECTIONS_BIT_NV = 16
    VK_OPTICAL_FLOW_SESSION_CREATE_ENABLE_COST_BIT_NV = 2
    VK_OPTICAL_FLOW_SESSION_CREATE_ENABLE_GLOBAL_FLOW_BIT_NV = 4
    VK_OPTICAL_FLOW_SESSION_CREATE_ENABLE_HINT_BIT_NV = 1

sys.modules[__name__] = VkOpticalFlowSessionCreateFlagsNV

