import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSamplerAddressMode(VulkanIntEnum):
    VK_SAMPLER_ADDRESS_MODE_MIRRORED_REPEAT = 1
    VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_EDGE = 2
    VK_SAMPLER_ADDRESS_MODE_MIRROR_CLAMP_TO_EDGE = 4
    VK_SAMPLER_ADDRESS_MODE_CLAMP_TO_BORDER = 3
    VK_SAMPLER_ADDRESS_MODE_REPEAT = 0

sys.modules[__name__] = VkSamplerAddressMode
