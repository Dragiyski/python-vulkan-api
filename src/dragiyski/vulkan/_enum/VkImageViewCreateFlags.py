import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkImageViewCreateFlags(VulkanUIntFlag):
    VK_IMAGE_VIEW_CREATE_DESCRIPTOR_BUFFER_CAPTURE_REPLAY_BIT_EXT = 4
    VK_IMAGE_VIEW_CREATE_FRAGMENT_DENSITY_MAP_DEFERRED_BIT_EXT = 2
    VK_IMAGE_VIEW_CREATE_FRAGMENT_DENSITY_MAP_DYNAMIC_BIT_EXT = 1

sys.modules[__name__] = VkImageViewCreateFlags

