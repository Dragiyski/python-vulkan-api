import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSciSyncPrimitiveTypeNV(VulkanIntEnum):
    VK_SCI_SYNC_PRIMITIVE_TYPE_FENCE_NV = 0
    VK_SCI_SYNC_PRIMITIVE_TYPE_SEMAPHORE_NV = 1

sys.modules[__name__] = VkSciSyncPrimitiveTypeNV

