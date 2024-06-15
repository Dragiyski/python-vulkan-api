import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkExternalFenceFeatureFlags(VulkanUIntFlag):
    VK_EXTERNAL_FENCE_FEATURE_EXPORTABLE_BIT = 1
    VK_EXTERNAL_FENCE_FEATURE_IMPORTABLE_BIT = 2

sys.modules[__name__] = VkExternalFenceFeatureFlags
