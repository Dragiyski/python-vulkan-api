import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSamplerYcbcrModelConversion(VulkanIntEnum):
    VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY = 0
    VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601 = 3
    VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709 = 2
    VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020 = 4
    VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY = 1

sys.modules[__name__] = VkSamplerYcbcrModelConversion
