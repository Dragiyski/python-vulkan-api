import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDescriptorBindingFlags(VulkanUIntFlag):
    VK_DESCRIPTOR_BINDING_UPDATE_UNUSED_WHILE_PENDING_BIT = 2
    VK_DESCRIPTOR_BINDING_UPDATE_AFTER_BIND_BIT = 1
    VK_DESCRIPTOR_BINDING_PARTIALLY_BOUND_BIT = 4
    VK_DESCRIPTOR_BINDING_VARIABLE_DESCRIPTOR_COUNT_BIT = 8

sys.modules[__name__] = VkDescriptorBindingFlags