import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkDeviceFaultVendorBinaryHeaderVersionEXT(VulkanIntEnum):
    VK_DEVICE_FAULT_VENDOR_BINARY_HEADER_VERSION_ONE_EXT = 1

sys.modules[__name__] = VkDeviceFaultVendorBinaryHeaderVersionEXT

