import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSemaphoreImportFlags(VulkanUIntFlag):
    VK_SEMAPHORE_IMPORT_TEMPORARY_BIT = 1

sys.modules[__name__] = VkSemaphoreImportFlags

VkSemaphoreImportFlags.VK_SEMAPHORE_IMPORT_TEMPORARY_BIT_KHR = VkSemaphoreImportFlags.VK_SEMAPHORE_IMPORT_TEMPORARY_BIT
