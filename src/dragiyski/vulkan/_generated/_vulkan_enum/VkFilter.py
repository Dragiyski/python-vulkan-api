import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkFilter(VulkanIntEnum):
    VK_FILTER_CUBIC_EXT = 1000015000
    VK_FILTER_LINEAR = 1
    VK_FILTER_NEAREST = 0

sys.modules[__name__] = VkFilter

VkFilter.VK_FILTER_CUBIC_IMG = VkFilter.VK_FILTER_CUBIC_EXT
