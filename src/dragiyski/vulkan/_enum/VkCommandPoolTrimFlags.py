import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkCommandPoolTrimFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkCommandPoolTrimFlags
