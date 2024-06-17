import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkQueryPoolCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkQueryPoolCreateFlags

