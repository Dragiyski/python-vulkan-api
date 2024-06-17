import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkOpacityMicromapFormatEXT(VulkanIntEnum):
    VK_OPACITY_MICROMAP_FORMAT_2_STATE_EXT = 1
    VK_OPACITY_MICROMAP_FORMAT_4_STATE_EXT = 2

sys.modules[__name__] = VkOpacityMicromapFormatEXT

