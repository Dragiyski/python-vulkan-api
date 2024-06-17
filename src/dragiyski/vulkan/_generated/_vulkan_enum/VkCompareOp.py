import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkCompareOp(VulkanIntEnum):
    VK_COMPARE_OP_ALWAYS = 7
    VK_COMPARE_OP_EQUAL = 2
    VK_COMPARE_OP_GREATER = 4
    VK_COMPARE_OP_GREATER_OR_EQUAL = 6
    VK_COMPARE_OP_LESS = 1
    VK_COMPARE_OP_LESS_OR_EQUAL = 3
    VK_COMPARE_OP_NEVER = 0
    VK_COMPARE_OP_NOT_EQUAL = 5

sys.modules[__name__] = VkCompareOp

