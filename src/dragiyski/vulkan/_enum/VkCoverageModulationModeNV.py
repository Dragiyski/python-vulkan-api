import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkCoverageModulationModeNV(VulkanIntEnum):
    VK_COVERAGE_MODULATION_MODE_RGBA_NV = 3
    VK_COVERAGE_MODULATION_MODE_NONE_NV = 0
    VK_COVERAGE_MODULATION_MODE_RGB_NV = 1
    VK_COVERAGE_MODULATION_MODE_ALPHA_NV = 2

sys.modules[__name__] = VkCoverageModulationModeNV
