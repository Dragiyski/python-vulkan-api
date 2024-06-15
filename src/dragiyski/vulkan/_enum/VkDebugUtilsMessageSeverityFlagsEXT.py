import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDebugUtilsMessageSeverityFlagsEXT(VulkanUIntFlag):
    VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT = 4096
    VK_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT = 16
    VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT = 1
    VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT = 256

sys.modules[__name__] = VkDebugUtilsMessageSeverityFlagsEXT

