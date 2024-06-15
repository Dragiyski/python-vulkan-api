import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkVideoDecodeCapabilityFlagsKHR(VulkanUIntFlag):
    VK_VIDEO_DECODE_CAPABILITY_DPB_AND_OUTPUT_COINCIDE_BIT_KHR = 1
    VK_VIDEO_DECODE_CAPABILITY_DPB_AND_OUTPUT_DISTINCT_BIT_KHR = 2

sys.modules[__name__] = VkVideoDecodeCapabilityFlagsKHR

