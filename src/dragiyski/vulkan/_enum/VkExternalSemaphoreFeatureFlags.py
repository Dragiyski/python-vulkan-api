import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkExternalSemaphoreFeatureFlags(VulkanUIntFlag):
    VK_EXTERNAL_SEMAPHORE_FEATURE_IMPORTABLE_BIT = 2
    VK_EXTERNAL_SEMAPHORE_FEATURE_EXPORTABLE_BIT = 1

sys.modules[__name__] = VkExternalSemaphoreFeatureFlags
