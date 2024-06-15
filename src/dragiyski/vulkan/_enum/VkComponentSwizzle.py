import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkComponentSwizzle(VulkanIntEnum):
    VK_COMPONENT_SWIZZLE_A = 6
    VK_COMPONENT_SWIZZLE_B = 5
    VK_COMPONENT_SWIZZLE_G = 4
    VK_COMPONENT_SWIZZLE_IDENTITY = 0
    VK_COMPONENT_SWIZZLE_ONE = 2
    VK_COMPONENT_SWIZZLE_R = 3
    VK_COMPONENT_SWIZZLE_ZERO = 1

sys.modules[__name__] = VkComponentSwizzle

