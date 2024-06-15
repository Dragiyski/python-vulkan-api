import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPeerMemoryFeatureFlags(VulkanUIntFlag):
    VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT = 1
    VK_PEER_MEMORY_FEATURE_COPY_DST_BIT = 2
    VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT = 8
    VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT = 4

sys.modules[__name__] = VkPeerMemoryFeatureFlags
