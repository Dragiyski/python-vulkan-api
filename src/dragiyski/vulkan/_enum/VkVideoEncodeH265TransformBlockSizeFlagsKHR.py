import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoEncodeH265TransformBlockSizeFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_H265_TRANSFORM_BLOCK_SIZE_16_BIT_KHR = 4
    VK_VIDEO_ENCODE_H265_TRANSFORM_BLOCK_SIZE_32_BIT_KHR = 8
    VK_VIDEO_ENCODE_H265_TRANSFORM_BLOCK_SIZE_8_BIT_KHR = 2
    VK_VIDEO_ENCODE_H265_TRANSFORM_BLOCK_SIZE_4_BIT_KHR = 1

sys.modules[__name__] = VkVideoEncodeH265TransformBlockSizeFlagsKHR
