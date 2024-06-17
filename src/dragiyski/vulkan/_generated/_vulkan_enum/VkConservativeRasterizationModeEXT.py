import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkConservativeRasterizationModeEXT(VulkanIntEnum):
    VK_CONSERVATIVE_RASTERIZATION_MODE_DISABLED_EXT = 0
    VK_CONSERVATIVE_RASTERIZATION_MODE_OVERESTIMATE_EXT = 1
    VK_CONSERVATIVE_RASTERIZATION_MODE_UNDERESTIMATE_EXT = 2

sys.modules[__name__] = VkConservativeRasterizationModeEXT

