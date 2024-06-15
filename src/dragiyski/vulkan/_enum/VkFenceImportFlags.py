import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkFenceImportFlags(VulkanUIntFlag):
    VK_FENCE_IMPORT_TEMPORARY_BIT = 1

sys.modules[__name__] = VkFenceImportFlags
