import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDeviceEventTypeEXT(VulkanIntEnum):
    VK_DEVICE_EVENT_TYPE_DISPLAY_HOTPLUG_EXT = 0

sys.modules[__name__] = VkDeviceEventTypeEXT

