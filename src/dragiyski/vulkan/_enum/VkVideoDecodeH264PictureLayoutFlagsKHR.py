import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoDecodeH264PictureLayoutFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_DECODE_H264_PICTURE_LAYOUT_PROGRESSIVE_KHR = 0
    VK_VIDEO_DECODE_H264_PICTURE_LAYOUT_INTERLACED_INTERLEAVED_LINES_BIT_KHR = 1
    VK_VIDEO_DECODE_H264_PICTURE_LAYOUT_INTERLACED_SEPARATE_PLANES_BIT_KHR = 2

sys.modules[__name__] = VkVideoDecodeH264PictureLayoutFlagsKHR
