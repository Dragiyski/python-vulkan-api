import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class StdVideoH265ChromaFormatIdc(VulkanIntEnum):
    STD_VIDEO_H265_CHROMA_FORMAT_IDC_420 = 1
    STD_VIDEO_H265_CHROMA_FORMAT_IDC_INVALID = 2147483647
    STD_VIDEO_H265_CHROMA_FORMAT_IDC_444 = 3
    STD_VIDEO_H265_CHROMA_FORMAT_IDC_MONOCHROME = 0
    STD_VIDEO_H265_CHROMA_FORMAT_IDC_422 = 2

sys.modules[__name__] = StdVideoH265ChromaFormatIdc
