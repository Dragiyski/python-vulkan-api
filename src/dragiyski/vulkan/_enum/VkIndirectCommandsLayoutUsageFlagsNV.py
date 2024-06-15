import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkIndirectCommandsLayoutUsageFlagsNV(VulkanUIntFlag):
    VK_INDIRECT_COMMANDS_LAYOUT_USAGE_EXPLICIT_PREPROCESS_BIT_NV = 1
    VK_INDIRECT_COMMANDS_LAYOUT_USAGE_UNORDERED_SEQUENCES_BIT_NV = 4
    VK_INDIRECT_COMMANDS_LAYOUT_USAGE_INDEXED_SEQUENCES_BIT_NV = 2

sys.modules[__name__] = VkIndirectCommandsLayoutUsageFlagsNV
