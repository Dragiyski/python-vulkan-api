import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkViewportCoordinateSwizzleNV(VulkanIntEnum):
    VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_W_NV = 6
    VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Z_NV = 4
    VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Y_NV = 3
    VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_W_NV = 7
    VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_X_NV = 0
    VK_VIEWPORT_COORDINATE_SWIZZLE_POSITIVE_Y_NV = 2
    VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_Z_NV = 5
    VK_VIEWPORT_COORDINATE_SWIZZLE_NEGATIVE_X_NV = 1

sys.modules[__name__] = VkViewportCoordinateSwizzleNV
