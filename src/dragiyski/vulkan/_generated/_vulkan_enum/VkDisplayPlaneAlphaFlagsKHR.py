import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkDisplayPlaneAlphaFlagsKHR(VulkanUIntFlag):
    VK_DISPLAY_PLANE_ALPHA_GLOBAL_BIT_KHR = 2
    VK_DISPLAY_PLANE_ALPHA_OPAQUE_BIT_KHR = 1
    VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_BIT_KHR = 4
    VK_DISPLAY_PLANE_ALPHA_PER_PIXEL_PREMULTIPLIED_BIT_KHR = 8

sys.modules[__name__] = VkDisplayPlaneAlphaFlagsKHR

