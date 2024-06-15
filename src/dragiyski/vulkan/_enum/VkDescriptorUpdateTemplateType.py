import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDescriptorUpdateTemplateType(VulkanIntEnum):
    VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET = 0
    VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_PUSH_DESCRIPTORS_KHR = 1

sys.modules[__name__] = VkDescriptorUpdateTemplateType

VkDescriptorUpdateTemplateType.VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET_KHR = VkDescriptorUpdateTemplateType.VK_DESCRIPTOR_UPDATE_TEMPLATE_TYPE_DESCRIPTOR_SET
