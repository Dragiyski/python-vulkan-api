import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkMemoryAllocateFlags(VulkanUIntFlag):
    VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_CAPTURE_REPLAY_BIT = 4
    VK_MEMORY_ALLOCATE_DEVICE_MASK_BIT = 1
    VK_MEMORY_ALLOCATE_DEVICE_ADDRESS_BIT = 2

sys.modules[__name__] = VkMemoryAllocateFlags
