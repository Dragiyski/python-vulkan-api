import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSciSyncClientTypeNV(VulkanIntEnum):
    VK_SCI_SYNC_CLIENT_TYPE_SIGNALER_NV = 0
    VK_SCI_SYNC_CLIENT_TYPE_SIGNALER_WAITER_NV = 2
    VK_SCI_SYNC_CLIENT_TYPE_WAITER_NV = 1

sys.modules[__name__] = VkSciSyncClientTypeNV

