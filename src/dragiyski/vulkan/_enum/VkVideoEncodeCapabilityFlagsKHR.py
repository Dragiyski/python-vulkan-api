import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoEncodeCapabilityFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_ENCODE_CAPABILITY_INSUFFICIENT_BITSTREAM_BUFFER_RANGE_DETECTION_BIT_KHR = 2
    VK_VIDEO_ENCODE_CAPABILITY_PRECEDING_EXTERNALLY_ENCODED_BYTES_BIT_KHR = 1

sys.modules[__name__] = VkVideoEncodeCapabilityFlagsKHR

