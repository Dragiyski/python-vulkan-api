import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDeviceCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkDeviceCreateFlags

