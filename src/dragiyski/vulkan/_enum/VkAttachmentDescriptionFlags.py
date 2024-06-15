import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkAttachmentDescriptionFlags(VulkanUIntFlag):
    VK_ATTACHMENT_DESCRIPTION_MAY_ALIAS_BIT = 1

sys.modules[__name__] = VkAttachmentDescriptionFlags

