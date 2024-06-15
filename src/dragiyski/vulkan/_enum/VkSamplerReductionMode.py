import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSamplerReductionMode(VulkanIntEnum):
    VK_SAMPLER_REDUCTION_MODE_MAX = 2
    VK_SAMPLER_REDUCTION_MODE_MIN = 1
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE = 0
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE_RANGECLAMP_QCOM = 1000521000

sys.modules[__name__] = VkSamplerReductionMode

VkSamplerReductionMode.VK_SAMPLER_REDUCTION_MODE_MAX_EXT = VkSamplerReductionMode.VK_SAMPLER_REDUCTION_MODE_MAX
VkSamplerReductionMode.VK_SAMPLER_REDUCTION_MODE_MIN_EXT = VkSamplerReductionMode.VK_SAMPLER_REDUCTION_MODE_MIN
VkSamplerReductionMode.VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE_EXT = VkSamplerReductionMode.VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE
