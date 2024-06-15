import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkScopeKHR(VulkanIntEnum):
    VK_SCOPE_DEVICE_KHR = 1
    VK_SCOPE_QUEUE_FAMILY_KHR = 5
    VK_SCOPE_SUBGROUP_KHR = 3
    VK_SCOPE_WORKGROUP_KHR = 2

sys.modules[__name__] = VkScopeKHR

VkScopeKHR.VK_SCOPE_DEVICE_NV = VkScopeKHR.VK_SCOPE_DEVICE_KHR
VkScopeKHR.VK_SCOPE_QUEUE_FAMILY_NV = VkScopeKHR.VK_SCOPE_QUEUE_FAMILY_KHR
VkScopeKHR.VK_SCOPE_SUBGROUP_NV = VkScopeKHR.VK_SCOPE_SUBGROUP_KHR
VkScopeKHR.VK_SCOPE_WORKGROUP_NV = VkScopeKHR.VK_SCOPE_WORKGROUP_KHR
