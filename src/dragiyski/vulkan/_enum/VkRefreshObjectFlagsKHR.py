import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkRefreshObjectFlagsKHR(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkRefreshObjectFlagsKHR
