import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkFragmentShadingRateTypeNV(VulkanIntEnum):
    VK_FRAGMENT_SHADING_RATE_TYPE_ENUMS_NV = 1
    VK_FRAGMENT_SHADING_RATE_TYPE_FRAGMENT_SIZE_NV = 0

sys.modules[__name__] = VkFragmentShadingRateTypeNV

