import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkMemoryUnmapFlagsKHR(VulkanUIntFlag):
    VK_MEMORY_UNMAP_RESERVE_BIT_EXT = 1

sys.modules[__name__] = VkMemoryUnmapFlagsKHR

