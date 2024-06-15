import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkMicromapTypeEXT(VulkanIntEnum):
    VK_MICROMAP_TYPE_OPACITY_MICROMAP_EXT = 0
    VK_MICROMAP_TYPE_DISPLACEMENT_MICROMAP_NV = 1000397000

sys.modules[__name__] = VkMicromapTypeEXT
