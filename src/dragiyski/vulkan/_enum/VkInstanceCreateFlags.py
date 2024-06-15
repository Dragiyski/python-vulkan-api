import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkInstanceCreateFlags(VulkanUIntFlag):
    VK_INSTANCE_CREATE_ENUMERATE_PORTABILITY_BIT_KHR = 1

sys.modules[__name__] = VkInstanceCreateFlags
