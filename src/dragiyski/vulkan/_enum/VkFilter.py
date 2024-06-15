import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkFilter(VulkanIntEnum):
    VK_FILTER_CUBIC_EXT = 1000015000
    VK_FILTER_NEAREST = 0
    VK_FILTER_LINEAR = 1

sys.modules[__name__] = VkFilter
