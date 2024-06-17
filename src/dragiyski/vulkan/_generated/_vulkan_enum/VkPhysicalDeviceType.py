import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkPhysicalDeviceType(VulkanIntEnum):
    VK_PHYSICAL_DEVICE_TYPE_CPU = 4
    VK_PHYSICAL_DEVICE_TYPE_DISCRETE_GPU = 2
    VK_PHYSICAL_DEVICE_TYPE_INTEGRATED_GPU = 1
    VK_PHYSICAL_DEVICE_TYPE_OTHER = 0
    VK_PHYSICAL_DEVICE_TYPE_VIRTUAL_GPU = 3

sys.modules[__name__] = VkPhysicalDeviceType

