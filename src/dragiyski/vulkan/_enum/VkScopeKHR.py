import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkScopeKHR(VulkanIntEnum):
    VK_SCOPE_WORKGROUP_KHR = 2
    VK_SCOPE_QUEUE_FAMILY_KHR = 5
    VK_SCOPE_DEVICE_KHR = 1
    VK_SCOPE_SUBGROUP_KHR = 3

sys.modules[__name__] = VkScopeKHR
