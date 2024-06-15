import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkMemoryHeapFlags(VulkanUIntFlag):
    VK_MEMORY_HEAP_DEVICE_LOCAL_BIT = 1
    VK_MEMORY_HEAP_MULTI_INSTANCE_BIT = 2

sys.modules[__name__] = VkMemoryHeapFlags

VkMemoryHeapFlags.VK_MEMORY_HEAP_MULTI_INSTANCE_BIT_KHR = VkMemoryHeapFlags.VK_MEMORY_HEAP_MULTI_INSTANCE_BIT
