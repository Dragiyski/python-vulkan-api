import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkMemoryHeapFlags(VulkanUIntFlag):
    VK_MEMORY_HEAP_MULTI_INSTANCE_BIT = 2
    VK_MEMORY_HEAP_DEVICE_LOCAL_BIT = 1

sys.modules[__name__] = VkMemoryHeapFlags
