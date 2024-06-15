import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkLineRasterizationModeKHR(VulkanIntEnum):
    VK_LINE_RASTERIZATION_MODE_BRESENHAM_KHR = 2
    VK_LINE_RASTERIZATION_MODE_DEFAULT_KHR = 0
    VK_LINE_RASTERIZATION_MODE_RECTANGULAR_KHR = 1
    VK_LINE_RASTERIZATION_MODE_RECTANGULAR_SMOOTH_KHR = 3

sys.modules[__name__] = VkLineRasterizationModeKHR
