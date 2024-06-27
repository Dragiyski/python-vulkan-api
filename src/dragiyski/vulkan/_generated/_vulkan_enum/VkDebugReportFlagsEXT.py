from enum import IntFlag

class VkDebugReportFlagsEXT(IntFlag):
    VK_DEBUG_REPORT_DEBUG_BIT_EXT = 16
    VK_DEBUG_REPORT_ERROR_BIT_EXT = 8
    VK_DEBUG_REPORT_INFORMATION_BIT_EXT = 1
    VK_DEBUG_REPORT_PERFORMANCE_WARNING_BIT_EXT = 4
    VK_DEBUG_REPORT_WARNING_BIT_EXT = 2