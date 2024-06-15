import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPolygonMode(VulkanIntEnum):
    VK_POLYGON_MODE_FILL = 0
    VK_POLYGON_MODE_FILL_RECTANGLE_NV = 1000153000
    VK_POLYGON_MODE_LINE = 1
    VK_POLYGON_MODE_POINT = 2

sys.modules[__name__] = VkPolygonMode

