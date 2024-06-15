import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSubpassContents(VulkanIntEnum):
    VK_SUBPASS_CONTENTS_SECONDARY_COMMAND_BUFFERS = 1
    VK_SUBPASS_CONTENTS_INLINE = 0
    VK_SUBPASS_CONTENTS_INLINE_AND_SECONDARY_COMMAND_BUFFERS_EXT = 1000451000

sys.modules[__name__] = VkSubpassContents
