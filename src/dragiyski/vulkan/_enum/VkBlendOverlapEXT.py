import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkBlendOverlapEXT(VulkanIntEnum):
    VK_BLEND_OVERLAP_DISJOINT_EXT = 1
    VK_BLEND_OVERLAP_CONJOINT_EXT = 2
    VK_BLEND_OVERLAP_UNCORRELATED_EXT = 0

sys.modules[__name__] = VkBlendOverlapEXT
