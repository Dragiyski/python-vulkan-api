import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkCoverageReductionModeNV(VulkanIntEnum):
    VK_COVERAGE_REDUCTION_MODE_MERGE_NV = 0
    VK_COVERAGE_REDUCTION_MODE_TRUNCATE_NV = 1

sys.modules[__name__] = VkCoverageReductionModeNV

