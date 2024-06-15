import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkFragmentShadingRateCombinerOpKHR(VulkanIntEnum):
    VK_FRAGMENT_SHADING_RATE_COMBINER_OP_REPLACE_KHR = 1
    VK_FRAGMENT_SHADING_RATE_COMBINER_OP_KEEP_KHR = 0
    VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MAX_KHR = 3
    VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MIN_KHR = 2
    VK_FRAGMENT_SHADING_RATE_COMBINER_OP_MUL_KHR = 4

sys.modules[__name__] = VkFragmentShadingRateCombinerOpKHR
