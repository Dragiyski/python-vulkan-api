import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoEncodeContentFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_CONTENT_CAMERA_BIT_KHR = 1
    VK_VIDEO_ENCODE_CONTENT_DEFAULT_KHR = 0
    VK_VIDEO_ENCODE_CONTENT_DESKTOP_BIT_KHR = 2
    VK_VIDEO_ENCODE_CONTENT_RENDERED_BIT_KHR = 4

sys.modules[__name__] = VkVideoEncodeContentFlagsKHR

