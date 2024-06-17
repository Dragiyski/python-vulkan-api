import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkExternalMemoryFeatureFlagsNV(VulkanUIntFlag):
    VK_EXTERNAL_MEMORY_FEATURE_DEDICATED_ONLY_BIT_NV = 1
    VK_EXTERNAL_MEMORY_FEATURE_EXPORTABLE_BIT_NV = 2
    VK_EXTERNAL_MEMORY_FEATURE_IMPORTABLE_BIT_NV = 4

sys.modules[__name__] = VkExternalMemoryFeatureFlagsNV

