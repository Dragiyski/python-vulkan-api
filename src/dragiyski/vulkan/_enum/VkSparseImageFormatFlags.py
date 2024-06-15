import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSparseImageFormatFlags(VulkanUIntFlag):
    VK_SPARSE_IMAGE_FORMAT_ALIGNED_MIP_SIZE_BIT = 2
    VK_SPARSE_IMAGE_FORMAT_NONSTANDARD_BLOCK_SIZE_BIT = 4
    VK_SPARSE_IMAGE_FORMAT_SINGLE_MIPTAIL_BIT = 1

sys.modules[__name__] = VkSparseImageFormatFlags

