import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkVideoEncodeH265CtbSizeFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_H265_CTB_SIZE_16_BIT_KHR = 1
    VK_VIDEO_ENCODE_H265_CTB_SIZE_32_BIT_KHR = 2
    VK_VIDEO_ENCODE_H265_CTB_SIZE_64_BIT_KHR = 4

sys.modules[__name__] = VkVideoEncodeH265CtbSizeFlagsKHR

