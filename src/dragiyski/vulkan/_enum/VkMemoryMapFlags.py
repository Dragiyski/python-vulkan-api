import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkMemoryMapFlags(VulkanUIntFlag):
    VK_MEMORY_MAP_PLACED_BIT_EXT = 1

sys.modules[__name__] = VkMemoryMapFlags
