import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkExternalMemoryFeatureFlags(VulkanUIntFlag):
    VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT = 4
    VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT = 2
    VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT = 1

sys.modules[__name__] = VkExternalMemoryFeatureFlags
