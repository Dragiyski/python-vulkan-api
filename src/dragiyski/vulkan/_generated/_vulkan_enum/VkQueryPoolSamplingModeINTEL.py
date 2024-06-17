import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkQueryPoolSamplingModeINTEL(VulkanIntEnum):
    VK_QUERY_POOL_SAMPLING_MODE_MANUAL_INTEL = 0

sys.modules[__name__] = VkQueryPoolSamplingModeINTEL

