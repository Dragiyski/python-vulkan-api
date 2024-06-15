import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkFramebufferCreateFlags(VulkanUIntFlag):
    VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT = 1

sys.modules[__name__] = VkFramebufferCreateFlags

VkFramebufferCreateFlags.VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT_KHR = VkFramebufferCreateFlags.VK_FRAMEBUFFER_CREATE_IMAGELESS_BIT
