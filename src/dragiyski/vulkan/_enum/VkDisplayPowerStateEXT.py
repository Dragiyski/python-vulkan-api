import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDisplayPowerStateEXT(VulkanIntEnum):
    VK_DISPLAY_POWER_STATE_OFF_EXT = 0
    VK_DISPLAY_POWER_STATE_ON_EXT = 2
    VK_DISPLAY_POWER_STATE_SUSPEND_EXT = 1

sys.modules[__name__] = VkDisplayPowerStateEXT

