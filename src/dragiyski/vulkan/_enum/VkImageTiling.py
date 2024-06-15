import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkImageTiling(VulkanIntEnum):
    VK_IMAGE_TILING_DRM_FORMAT_MODIFIER_EXT = 1000158000
    VK_IMAGE_TILING_LINEAR = 1
    VK_IMAGE_TILING_OPTIMAL = 0

sys.modules[__name__] = VkImageTiling

