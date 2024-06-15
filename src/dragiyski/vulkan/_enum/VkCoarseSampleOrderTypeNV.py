import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkCoarseSampleOrderTypeNV(VulkanIntEnum):
    VK_COARSE_SAMPLE_ORDER_TYPE_DEFAULT_NV = 0
    VK_COARSE_SAMPLE_ORDER_TYPE_CUSTOM_NV = 1
    VK_COARSE_SAMPLE_ORDER_TYPE_PIXEL_MAJOR_NV = 2
    VK_COARSE_SAMPLE_ORDER_TYPE_SAMPLE_MAJOR_NV = 3

sys.modules[__name__] = VkCoarseSampleOrderTypeNV
