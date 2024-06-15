import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSamplerReductionMode(VulkanIntEnum):
    VK_SAMPLER_REDUCTION_MODE_MAX = 2
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE = 0
    VK_SAMPLER_REDUCTION_MODE_WEIGHTED_AVERAGE_RANGECLAMP_QCOM = 1000521000
    VK_SAMPLER_REDUCTION_MODE_MIN = 1

sys.modules[__name__] = VkSamplerReductionMode
