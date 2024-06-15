import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkOpticalFlowGridSizeFlagsNV(VulkanUIntFlag):
    VK_OPTICAL_FLOW_GRID_SIZE_1X1_BIT_NV = 1
    VK_OPTICAL_FLOW_GRID_SIZE_2X2_BIT_NV = 2
    VK_OPTICAL_FLOW_GRID_SIZE_4X4_BIT_NV = 4
    VK_OPTICAL_FLOW_GRID_SIZE_8X8_BIT_NV = 8
    VK_OPTICAL_FLOW_GRID_SIZE_UNKNOWN_NV = 0

sys.modules[__name__] = VkOpticalFlowGridSizeFlagsNV

