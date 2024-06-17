import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkHostImageCopyFlagsEXT(VulkanUIntFlag):
    VK_HOST_IMAGE_COPY_MEMCPY_EXT = 1

sys.modules[__name__] = VkHostImageCopyFlagsEXT

