import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkImageAspectFlags(VulkanUIntFlag):
    VK_IMAGE_ASPECT_COLOR_BIT = 1
    VK_IMAGE_ASPECT_DEPTH_BIT = 2
    VK_IMAGE_ASPECT_MEMORY_PLANE_0_BIT_EXT = 128
    VK_IMAGE_ASPECT_MEMORY_PLANE_1_BIT_EXT = 256
    VK_IMAGE_ASPECT_MEMORY_PLANE_2_BIT_EXT = 512
    VK_IMAGE_ASPECT_MEMORY_PLANE_3_BIT_EXT = 1024
    VK_IMAGE_ASPECT_METADATA_BIT = 8
    VK_IMAGE_ASPECT_NONE = 0
    VK_IMAGE_ASPECT_PLANE_0_BIT = 16
    VK_IMAGE_ASPECT_PLANE_1_BIT = 32
    VK_IMAGE_ASPECT_PLANE_2_BIT = 64
    VK_IMAGE_ASPECT_STENCIL_BIT = 4

sys.modules[__name__] = VkImageAspectFlags

VkImageAspectFlags.VK_IMAGE_ASPECT_NONE_KHR = VkImageAspectFlags.VK_IMAGE_ASPECT_NONE
VkImageAspectFlags.VK_IMAGE_ASPECT_PLANE_0_BIT_KHR = VkImageAspectFlags.VK_IMAGE_ASPECT_PLANE_0_BIT
VkImageAspectFlags.VK_IMAGE_ASPECT_PLANE_1_BIT_KHR = VkImageAspectFlags.VK_IMAGE_ASPECT_PLANE_1_BIT
VkImageAspectFlags.VK_IMAGE_ASPECT_PLANE_2_BIT_KHR = VkImageAspectFlags.VK_IMAGE_ASPECT_PLANE_2_BIT
