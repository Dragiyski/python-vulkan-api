import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSubmitFlags(VulkanUIntFlag):
    VK_SUBMIT_PROTECTED_BIT = 1

sys.modules[__name__] = VkSubmitFlags
