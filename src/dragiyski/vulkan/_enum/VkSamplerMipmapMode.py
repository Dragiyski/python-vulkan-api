import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSamplerMipmapMode(VulkanIntEnum):
    VK_SAMPLER_MIPMAP_MODE_NEAREST = 0
    VK_SAMPLER_MIPMAP_MODE_LINEAR = 1

sys.modules[__name__] = VkSamplerMipmapMode
