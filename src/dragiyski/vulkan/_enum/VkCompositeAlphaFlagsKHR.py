import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkCompositeAlphaFlagsKHR(VulkanUIntFlag):
    VK_COMPOSITE_ALPHA_INHERIT_BIT_KHR = 8
    VK_COMPOSITE_ALPHA_OPAQUE_BIT_KHR = 1
    VK_COMPOSITE_ALPHA_POST_MULTIPLIED_BIT_KHR = 4
    VK_COMPOSITE_ALPHA_PRE_MULTIPLIED_BIT_KHR = 2

sys.modules[__name__] = VkCompositeAlphaFlagsKHR

