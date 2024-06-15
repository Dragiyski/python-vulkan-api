import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoDecodeFlagsKHR(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkVideoDecodeFlagsKHR

