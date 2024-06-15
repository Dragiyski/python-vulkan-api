import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkCopyMicromapModeEXT(VulkanIntEnum):
    VK_COPY_MICROMAP_MODE_SERIALIZE_EXT = 1
    VK_COPY_MICROMAP_MODE_CLONE_EXT = 0
    VK_COPY_MICROMAP_MODE_DESERIALIZE_EXT = 2
    VK_COPY_MICROMAP_MODE_COMPACT_EXT = 3

sys.modules[__name__] = VkCopyMicromapModeEXT
