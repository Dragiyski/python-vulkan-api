import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoEncodeFeedbackFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_FEEDBACK_BITSTREAM_BUFFER_OFFSET_BIT_KHR = 1
    VK_VIDEO_ENCODE_FEEDBACK_BITSTREAM_BYTES_WRITTEN_BIT_KHR = 2
    VK_VIDEO_ENCODE_FEEDBACK_BITSTREAM_HAS_OVERRIDES_BIT_KHR = 4

sys.modules[__name__] = VkVideoEncodeFeedbackFlagsKHR

