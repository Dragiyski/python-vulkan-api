import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkFenceImportFlags(VulkanUIntFlag):
    VK_FENCE_IMPORT_TEMPORARY_BIT = 1

sys.modules[__name__] = VkFenceImportFlags

VkFenceImportFlags.VK_FENCE_IMPORT_TEMPORARY_BIT_KHR = VkFenceImportFlags.VK_FENCE_IMPORT_TEMPORARY_BIT
