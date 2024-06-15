import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoChromaSubsamplingFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_CHROMA_SUBSAMPLING_420_BIT_KHR = 2
    VK_VIDEO_CHROMA_SUBSAMPLING_422_BIT_KHR = 4
    VK_VIDEO_CHROMA_SUBSAMPLING_444_BIT_KHR = 8
    VK_VIDEO_CHROMA_SUBSAMPLING_INVALID_KHR = 0
    VK_VIDEO_CHROMA_SUBSAMPLING_MONOCHROME_BIT_KHR = 1

sys.modules[__name__] = VkVideoChromaSubsamplingFlagsKHR

