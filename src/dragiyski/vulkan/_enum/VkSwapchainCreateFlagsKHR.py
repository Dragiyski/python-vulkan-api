import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSwapchainCreateFlagsKHR(VulkanUIntFlag):
    VK_SWAPCHAIN_CREATE_DEFERRED_MEMORY_ALLOCATION_BIT_EXT = 8
    VK_SWAPCHAIN_CREATE_MUTABLE_FORMAT_BIT_KHR = 4
    VK_SWAPCHAIN_CREATE_PROTECTED_BIT_KHR = 2
    VK_SWAPCHAIN_CREATE_SPLIT_INSTANCE_BIND_REGIONS_BIT_KHR = 1

sys.modules[__name__] = VkSwapchainCreateFlagsKHR

