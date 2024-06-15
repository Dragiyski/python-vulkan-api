import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDebugReportFlagsEXT(VulkanUIntFlag):
    VK_DEBUG_REPORT_DEBUG_BIT_EXT = 16
    VK_DEBUG_REPORT_ERROR_BIT_EXT = 8
    VK_DEBUG_REPORT_INFORMATION_BIT_EXT = 1
    VK_DEBUG_REPORT_PERFORMANCE_WARNING_BIT_EXT = 4
    VK_DEBUG_REPORT_WARNING_BIT_EXT = 2

sys.modules[__name__] = VkDebugReportFlagsEXT

