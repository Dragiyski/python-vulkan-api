import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkDeviceGroupPresentModeFlagsKHR(VulkanUIntFlag):
    VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_BIT_KHR = 1
    VK_DEVICE_GROUP_PRESENT_MODE_LOCAL_MULTI_DEVICE_BIT_KHR = 8
    VK_DEVICE_GROUP_PRESENT_MODE_REMOTE_BIT_KHR = 2
    VK_DEVICE_GROUP_PRESENT_MODE_SUM_BIT_KHR = 4

sys.modules[__name__] = VkDeviceGroupPresentModeFlagsKHR

