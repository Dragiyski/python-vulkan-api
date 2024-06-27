from enum import IntFlag

class VkPeerMemoryFeatureFlags(IntFlag):
    VK_PEER_MEMORY_FEATURE_COPY_DST_BIT = 2
    VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT = 1
    VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT = 8
    VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT = 4
    VK_PEER_MEMORY_FEATURE_COPY_DST_BIT_KHR = VK_PEER_MEMORY_FEATURE_COPY_DST_BIT
    VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT_KHR = VK_PEER_MEMORY_FEATURE_COPY_SRC_BIT
    VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT_KHR = VK_PEER_MEMORY_FEATURE_GENERIC_DST_BIT
    VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT_KHR = VK_PEER_MEMORY_FEATURE_GENERIC_SRC_BIT