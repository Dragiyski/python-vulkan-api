import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkImageViewType(VulkanIntEnum):
    VK_IMAGE_VIEW_TYPE_1D = 0
    VK_IMAGE_VIEW_TYPE_3D = 2
    VK_IMAGE_VIEW_TYPE_CUBE = 3
    VK_IMAGE_VIEW_TYPE_2D = 1
    VK_IMAGE_VIEW_TYPE_CUBE_ARRAY = 6
    VK_IMAGE_VIEW_TYPE_2D_ARRAY = 5
    VK_IMAGE_VIEW_TYPE_1D_ARRAY = 4

sys.modules[__name__] = VkImageViewType
