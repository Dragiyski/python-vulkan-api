import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkDependencyFlags(VulkanUIntFlag):
    VK_DEPENDENCY_BY_REGION_BIT = 1
    VK_DEPENDENCY_DEVICE_GROUP_BIT = 4
    VK_DEPENDENCY_FEEDBACK_LOOP_BIT_EXT = 8
    VK_DEPENDENCY_VIEW_LOCAL_BIT = 2

sys.modules[__name__] = VkDependencyFlags

VkDependencyFlags.VK_DEPENDENCY_DEVICE_GROUP_BIT_KHR = VkDependencyFlags.VK_DEPENDENCY_DEVICE_GROUP_BIT
VkDependencyFlags.VK_DEPENDENCY_VIEW_LOCAL_BIT_KHR = VkDependencyFlags.VK_DEPENDENCY_VIEW_LOCAL_BIT
