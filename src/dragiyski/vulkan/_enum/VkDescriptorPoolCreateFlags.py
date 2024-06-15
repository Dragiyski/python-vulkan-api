import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDescriptorPoolCreateFlags(VulkanUIntFlag):
    VK_DESCRIPTOR_POOL_CREATE_ALLOW_OVERALLOCATION_POOLS_BIT_NV = 16
    VK_DESCRIPTOR_POOL_CREATE_ALLOW_OVERALLOCATION_SETS_BIT_NV = 8
    VK_DESCRIPTOR_POOL_CREATE_FREE_DESCRIPTOR_SET_BIT = 1
    VK_DESCRIPTOR_POOL_CREATE_HOST_ONLY_BIT_EXT = 4
    VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT = 2

sys.modules[__name__] = VkDescriptorPoolCreateFlags

VkDescriptorPoolCreateFlags.VK_DESCRIPTOR_POOL_CREATE_HOST_ONLY_BIT_VALVE = VkDescriptorPoolCreateFlags.VK_DESCRIPTOR_POOL_CREATE_HOST_ONLY_BIT_EXT
VkDescriptorPoolCreateFlags.VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT_EXT = VkDescriptorPoolCreateFlags.VK_DESCRIPTOR_POOL_CREATE_UPDATE_AFTER_BIND_BIT
