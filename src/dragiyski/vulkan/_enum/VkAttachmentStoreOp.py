import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkAttachmentStoreOp(VulkanIntEnum):
    VK_ATTACHMENT_STORE_OP_DONT_CARE = 1
    VK_ATTACHMENT_STORE_OP_NONE = 1000301000
    VK_ATTACHMENT_STORE_OP_STORE = 0

sys.modules[__name__] = VkAttachmentStoreOp
