import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkColorComponentFlags(VulkanUIntFlag):
    VK_COLOR_COMPONENT_B_BIT = 4
    VK_COLOR_COMPONENT_G_BIT = 2
    VK_COLOR_COMPONENT_R_BIT = 1
    VK_COLOR_COMPONENT_A_BIT = 8

sys.modules[__name__] = VkColorComponentFlags
