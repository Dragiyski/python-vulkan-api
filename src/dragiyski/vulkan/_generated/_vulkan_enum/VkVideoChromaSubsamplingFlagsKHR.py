from enum import IntFlag

class VkVideoChromaSubsamplingFlagsKHR(IntFlag):
    VK_VIDEO_CHROMA_SUBSAMPLING_420_BIT_KHR = 2
    VK_VIDEO_CHROMA_SUBSAMPLING_422_BIT_KHR = 4
    VK_VIDEO_CHROMA_SUBSAMPLING_444_BIT_KHR = 8
    VK_VIDEO_CHROMA_SUBSAMPLING_INVALID_KHR = 0
    VK_VIDEO_CHROMA_SUBSAMPLING_MONOCHROME_BIT_KHR = 1