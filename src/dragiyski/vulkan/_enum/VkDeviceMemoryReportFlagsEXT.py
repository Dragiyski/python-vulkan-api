import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDeviceMemoryReportFlagsEXT(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkDeviceMemoryReportFlagsEXT
