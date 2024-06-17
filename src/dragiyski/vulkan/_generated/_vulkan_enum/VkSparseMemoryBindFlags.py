import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkSparseMemoryBindFlags(VulkanUIntFlag):
    VK_SPARSE_MEMORY_BIND_METADATA_BIT = 1

sys.modules[__name__] = VkSparseMemoryBindFlags

