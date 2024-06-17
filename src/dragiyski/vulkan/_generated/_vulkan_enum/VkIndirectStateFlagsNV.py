import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkIndirectStateFlagsNV(VulkanUIntFlag):
    VK_INDIRECT_STATE_FLAG_FRONTFACE_BIT_NV = 1

sys.modules[__name__] = VkIndirectStateFlagsNV

