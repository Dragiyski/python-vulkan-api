import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkAttachmentLoadOp(VulkanIntEnum):
    VK_ATTACHMENT_LOAD_OP_DONT_CARE = 2
    VK_ATTACHMENT_LOAD_OP_CLEAR = 1
    VK_ATTACHMENT_LOAD_OP_LOAD = 0
    VK_ATTACHMENT_LOAD_OP_NONE_KHR = 1000400000

sys.modules[__name__] = VkAttachmentLoadOp
