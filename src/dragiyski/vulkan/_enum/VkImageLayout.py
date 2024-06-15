import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkImageLayout(VulkanIntEnum):
    VK_IMAGE_LAYOUT_ATTACHMENT_FEEDBACK_LOOP_OPTIMAL_EXT = 1000339000
    VK_IMAGE_LAYOUT_ATTACHMENT_OPTIMAL = 1000314001
    VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL = 2
    VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL = 1000241000
    VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL = 1000117001
    VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL = 1000241001
    VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL = 1000117000
    VK_IMAGE_LAYOUT_DEPTH_STENCIL_ATTACHMENT_OPTIMAL = 3
    VK_IMAGE_LAYOUT_DEPTH_STENCIL_READ_ONLY_OPTIMAL = 4
    VK_IMAGE_LAYOUT_FRAGMENT_DENSITY_MAP_OPTIMAL_EXT = 1000218000
    VK_IMAGE_LAYOUT_FRAGMENT_SHADING_RATE_ATTACHMENT_OPTIMAL_KHR = 1000164003
    VK_IMAGE_LAYOUT_GENERAL = 1
    VK_IMAGE_LAYOUT_PREINITIALIZED = 8
    VK_IMAGE_LAYOUT_PRESENT_SRC_KHR = 1000001002
    VK_IMAGE_LAYOUT_READ_ONLY_OPTIMAL = 1000314000
    VK_IMAGE_LAYOUT_RENDERING_LOCAL_READ_KHR = 1000232000
    VK_IMAGE_LAYOUT_SHADER_READ_ONLY_OPTIMAL = 5
    VK_IMAGE_LAYOUT_SHARED_PRESENT_KHR = 1000111000
    VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL = 1000241002
    VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL = 1000241003
    VK_IMAGE_LAYOUT_TRANSFER_DST_OPTIMAL = 7
    VK_IMAGE_LAYOUT_TRANSFER_SRC_OPTIMAL = 6
    VK_IMAGE_LAYOUT_UNDEFINED = 0
    VK_IMAGE_LAYOUT_VIDEO_DECODE_DPB_KHR = 1000024002
    VK_IMAGE_LAYOUT_VIDEO_DECODE_DST_KHR = 1000024000
    VK_IMAGE_LAYOUT_VIDEO_DECODE_SRC_KHR = 1000024001
    VK_IMAGE_LAYOUT_VIDEO_ENCODE_DPB_KHR = 1000299002
    VK_IMAGE_LAYOUT_VIDEO_ENCODE_DST_KHR = 1000299000
    VK_IMAGE_LAYOUT_VIDEO_ENCODE_SRC_KHR = 1000299001

sys.modules[__name__] = VkImageLayout

VkImageLayout.VK_IMAGE_LAYOUT_ATTACHMENT_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_ATTACHMENT_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_ATTACHMENT_STENCIL_READ_ONLY_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_DEPTH_READ_ONLY_STENCIL_ATTACHMENT_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_READ_ONLY_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_READ_ONLY_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_SHADING_RATE_OPTIMAL_NV = VkImageLayout.VK_IMAGE_LAYOUT_FRAGMENT_SHADING_RATE_ATTACHMENT_OPTIMAL_KHR
VkImageLayout.VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_STENCIL_ATTACHMENT_OPTIMAL
VkImageLayout.VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL_KHR = VkImageLayout.VK_IMAGE_LAYOUT_STENCIL_READ_ONLY_OPTIMAL
