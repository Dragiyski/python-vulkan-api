import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPresentGravityFlagsEXT(VulkanUIntFlag):
    VK_PRESENT_GRAVITY_MIN_BIT_EXT = 1
    VK_PRESENT_GRAVITY_CENTERED_BIT_EXT = 4
    VK_PRESENT_GRAVITY_MAX_BIT_EXT = 2

sys.modules[__name__] = VkPresentGravityFlagsEXT
