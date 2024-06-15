import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSampleCountFlags(VulkanUIntFlag):
    VK_SAMPLE_COUNT_2_BIT = 2
    VK_SAMPLE_COUNT_4_BIT = 4
    VK_SAMPLE_COUNT_64_BIT = 64
    VK_SAMPLE_COUNT_8_BIT = 8
    VK_SAMPLE_COUNT_32_BIT = 32
    VK_SAMPLE_COUNT_1_BIT = 1
    VK_SAMPLE_COUNT_16_BIT = 16

sys.modules[__name__] = VkSampleCountFlags
