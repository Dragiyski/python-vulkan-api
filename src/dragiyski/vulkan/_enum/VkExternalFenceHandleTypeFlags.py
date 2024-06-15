import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkExternalFenceHandleTypeFlags(VulkanUIntFlag):
    VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT = 4
    VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_WIN32_BIT = 2
    VK_EXTERNAL_FENCE_HANDLE_TYPE_SYNC_FD_BIT = 8
    VK_EXTERNAL_FENCE_HANDLE_TYPE_OPAQUE_FD_BIT = 1

sys.modules[__name__] = VkExternalFenceHandleTypeFlags
