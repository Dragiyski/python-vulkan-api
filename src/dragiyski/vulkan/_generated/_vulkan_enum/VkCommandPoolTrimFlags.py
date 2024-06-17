import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkCommandPoolTrimFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkCommandPoolTrimFlags

