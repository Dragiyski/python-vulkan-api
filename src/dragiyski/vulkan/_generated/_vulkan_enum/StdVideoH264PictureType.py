import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class StdVideoH264PictureType(VulkanIntEnum):
    STD_VIDEO_H264_PICTURE_TYPE_B = 1
    STD_VIDEO_H264_PICTURE_TYPE_I = 2
    STD_VIDEO_H264_PICTURE_TYPE_IDR = 5
    STD_VIDEO_H264_PICTURE_TYPE_INVALID = 2147483647
    STD_VIDEO_H264_PICTURE_TYPE_P = 0

sys.modules[__name__] = StdVideoH264PictureType

