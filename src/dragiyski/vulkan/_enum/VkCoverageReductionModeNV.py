import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkCoverageReductionModeNV(VulkanIntEnum):
    VK_COVERAGE_REDUCTION_MODE_TRUNCATE_NV = 1
    VK_COVERAGE_REDUCTION_MODE_MERGE_NV = 0

sys.modules[__name__] = VkCoverageReductionModeNV
