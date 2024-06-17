import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkOpticalFlowExecuteFlagsNV(VulkanUIntFlag):
    VK_OPTICAL_FLOW_EXECUTE_DISABLE_TEMPORAL_HINTS_BIT_NV = 1

sys.modules[__name__] = VkOpticalFlowExecuteFlagsNV

