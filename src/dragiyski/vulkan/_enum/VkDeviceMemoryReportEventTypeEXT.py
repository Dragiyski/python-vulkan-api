import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDeviceMemoryReportEventTypeEXT(VulkanIntEnum):
    VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATE_EXT = 0
    VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_ALLOCATION_FAILED_EXT = 4
    VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_FREE_EXT = 1
    VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_UNIMPORT_EXT = 3
    VK_DEVICE_MEMORY_REPORT_EVENT_TYPE_IMPORT_EXT = 2

sys.modules[__name__] = VkDeviceMemoryReportEventTypeEXT