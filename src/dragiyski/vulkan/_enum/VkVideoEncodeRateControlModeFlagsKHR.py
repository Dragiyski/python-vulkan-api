import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoEncodeRateControlModeFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_RATE_CONTROL_MODE_DISABLED_BIT_KHR = 1
    VK_VIDEO_ENCODE_RATE_CONTROL_MODE_CBR_BIT_KHR = 2
    VK_VIDEO_ENCODE_RATE_CONTROL_MODE_VBR_BIT_KHR = 4
    VK_VIDEO_ENCODE_RATE_CONTROL_MODE_DEFAULT_KHR = 0

sys.modules[__name__] = VkVideoEncodeRateControlModeFlagsKHR
