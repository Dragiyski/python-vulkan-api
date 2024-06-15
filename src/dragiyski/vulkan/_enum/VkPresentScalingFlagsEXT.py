import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPresentScalingFlagsEXT(VulkanUIntFlag):
    VK_PRESENT_SCALING_ASPECT_RATIO_STRETCH_BIT_EXT = 2
    VK_PRESENT_SCALING_ONE_TO_ONE_BIT_EXT = 1
    VK_PRESENT_SCALING_STRETCH_BIT_EXT = 4

sys.modules[__name__] = VkPresentScalingFlagsEXT

