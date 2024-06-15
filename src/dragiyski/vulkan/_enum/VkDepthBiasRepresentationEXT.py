import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDepthBiasRepresentationEXT(VulkanIntEnum):
    VK_DEPTH_BIAS_REPRESENTATION_FLOAT_EXT = 2
    VK_DEPTH_BIAS_REPRESENTATION_LEAST_REPRESENTABLE_VALUE_FORCE_UNORM_EXT = 1
    VK_DEPTH_BIAS_REPRESENTATION_LEAST_REPRESENTABLE_VALUE_FORMAT_EXT = 0

sys.modules[__name__] = VkDepthBiasRepresentationEXT
