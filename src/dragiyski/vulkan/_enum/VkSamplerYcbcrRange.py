import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSamplerYcbcrRange(VulkanIntEnum):
    VK_SAMPLER_YCBCR_RANGE_ITU_FULL = 0
    VK_SAMPLER_YCBCR_RANGE_ITU_NARROW = 1

sys.modules[__name__] = VkSamplerYcbcrRange