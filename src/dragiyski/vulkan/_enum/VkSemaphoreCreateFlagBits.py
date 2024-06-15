import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSemaphoreCreateFlagBits(VulkanIntEnum):
    pass

sys.modules[__name__] = VkSemaphoreCreateFlagBits
