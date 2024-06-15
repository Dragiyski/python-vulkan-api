import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkQueryControlFlags(VulkanUIntFlag):
    VK_QUERY_CONTROL_PRECISE_BIT = 1

sys.modules[__name__] = VkQueryControlFlags
