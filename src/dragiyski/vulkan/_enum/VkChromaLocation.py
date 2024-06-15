import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkChromaLocation(VulkanIntEnum):
    VK_CHROMA_LOCATION_COSITED_EVEN = 0
    VK_CHROMA_LOCATION_MIDPOINT = 1

sys.modules[__name__] = VkChromaLocation
