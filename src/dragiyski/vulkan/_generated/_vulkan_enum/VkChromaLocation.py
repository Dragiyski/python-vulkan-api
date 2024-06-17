import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkChromaLocation(VulkanIntEnum):
    VK_CHROMA_LOCATION_COSITED_EVEN = 0
    VK_CHROMA_LOCATION_MIDPOINT = 1

sys.modules[__name__] = VkChromaLocation

VkChromaLocation.VK_CHROMA_LOCATION_COSITED_EVEN_KHR = VkChromaLocation.VK_CHROMA_LOCATION_COSITED_EVEN
VkChromaLocation.VK_CHROMA_LOCATION_MIDPOINT_KHR = VkChromaLocation.VK_CHROMA_LOCATION_MIDPOINT
