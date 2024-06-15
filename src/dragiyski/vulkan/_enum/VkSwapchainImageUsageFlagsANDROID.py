import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSwapchainImageUsageFlagsANDROID(VulkanUIntFlag):
    VK_SWAPCHAIN_IMAGE_USAGE_SHARED_BIT_ANDROID = 1

sys.modules[__name__] = VkSwapchainImageUsageFlagsANDROID

