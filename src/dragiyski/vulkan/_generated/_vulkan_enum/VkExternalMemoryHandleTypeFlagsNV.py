import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkExternalMemoryHandleTypeFlagsNV(VulkanUIntFlag):
    VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_BIT_NV = 4
    VK_EXTERNAL_MEMORY_HANDLE_TYPE_D3D11_IMAGE_KMT_BIT_NV = 8
    VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_BIT_NV = 1
    VK_EXTERNAL_MEMORY_HANDLE_TYPE_OPAQUE_WIN32_KMT_BIT_NV = 2

sys.modules[__name__] = VkExternalMemoryHandleTypeFlagsNV

