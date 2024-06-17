import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkVideoEncodeFlagsKHR(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkVideoEncodeFlagsKHR

