import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkBufferViewCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkBufferViewCreateFlags

