import ctypes, sys
from .._vulkan_base import VulkanULongFlag

class VkMemoryDecompressionMethodFlagsNV(VulkanULongFlag):
    VK_MEMORY_DECOMPRESSION_METHOD_GDEFLATE_1_0_BIT_NV = 1

sys.modules[__name__] = VkMemoryDecompressionMethodFlagsNV

