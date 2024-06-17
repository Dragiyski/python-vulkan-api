import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkRefreshObjectFlagsKHR(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkRefreshObjectFlagsKHR

