import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDebugUtilsMessageTypeFlagsEXT(VulkanUIntFlag):
    VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT = 2
    VK_DEBUG_UTILS_MESSAGE_TYPE_DEVICE_ADDRESS_BINDING_BIT_EXT = 8
    VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT = 4
    VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT = 1

sys.modules[__name__] = VkDebugUtilsMessageTypeFlagsEXT
