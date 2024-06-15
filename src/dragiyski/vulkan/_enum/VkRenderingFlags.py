import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkRenderingFlags(VulkanUIntFlag):
    VK_RENDERING_SUSPENDING_BIT = 2
    VK_RENDERING_RESUMING_BIT = 4
    VK_RENDERING_CONTENTS_SECONDARY_COMMAND_BUFFERS_BIT = 1
    VK_RENDERING_CONTENTS_INLINE_BIT_EXT = 16
    VK_RENDERING_ENABLE_LEGACY_DITHERING_BIT_EXT = 8

sys.modules[__name__] = VkRenderingFlags
