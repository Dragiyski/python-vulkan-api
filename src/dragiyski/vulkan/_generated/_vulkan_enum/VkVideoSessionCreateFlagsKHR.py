import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkVideoSessionCreateFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_SESSION_CREATE_ALLOW_ENCODE_PARAMETER_OPTIMIZATIONS_BIT_KHR = 2
    VK_VIDEO_SESSION_CREATE_INLINE_QUERIES_BIT_KHR = 4
    VK_VIDEO_SESSION_CREATE_PROTECTED_CONTENT_BIT_KHR = 1

sys.modules[__name__] = VkVideoSessionCreateFlagsKHR

