import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkImageType(VulkanIntEnum):
    VK_IMAGE_TYPE_1D = 0
    VK_IMAGE_TYPE_2D = 1
    VK_IMAGE_TYPE_3D = 2

sys.modules[__name__] = VkImageType

