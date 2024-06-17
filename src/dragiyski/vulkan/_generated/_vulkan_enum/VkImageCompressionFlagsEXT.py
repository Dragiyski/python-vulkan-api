import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkImageCompressionFlagsEXT(VulkanUIntFlag):
    VK_IMAGE_COMPRESSION_DEFAULT_EXT = 0
    VK_IMAGE_COMPRESSION_DISABLED_EXT = 4
    VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT = 1
    VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT = 2

sys.modules[__name__] = VkImageCompressionFlagsEXT

