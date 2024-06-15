import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPrivateDataSlotCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkPrivateDataSlotCreateFlags

