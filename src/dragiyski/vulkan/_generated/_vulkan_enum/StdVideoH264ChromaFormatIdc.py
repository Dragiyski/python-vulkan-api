import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class StdVideoH264ChromaFormatIdc(VulkanIntEnum):
    STD_VIDEO_H264_CHROMA_FORMAT_IDC_420 = 1
    STD_VIDEO_H264_CHROMA_FORMAT_IDC_422 = 2
    STD_VIDEO_H264_CHROMA_FORMAT_IDC_444 = 3
    STD_VIDEO_H264_CHROMA_FORMAT_IDC_INVALID = 2147483647
    STD_VIDEO_H264_CHROMA_FORMAT_IDC_MONOCHROME = 0

sys.modules[__name__] = StdVideoH264ChromaFormatIdc

