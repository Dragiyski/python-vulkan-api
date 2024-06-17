import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkDescriptorPoolResetFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkDescriptorPoolResetFlags

