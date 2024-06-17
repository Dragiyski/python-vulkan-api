import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkDisplayEventTypeEXT(VulkanIntEnum):
    VK_DISPLAY_EVENT_TYPE_FIRST_PIXEL_OUT_EXT = 0

sys.modules[__name__] = VkDisplayEventTypeEXT

