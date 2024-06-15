import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkDisplacementMicromapFormatNV(VulkanIntEnum):
    VK_DISPLACEMENT_MICROMAP_FORMAT_1024_TRIANGLES_128_BYTES_NV = 3
    VK_DISPLACEMENT_MICROMAP_FORMAT_256_TRIANGLES_128_BYTES_NV = 2
    VK_DISPLACEMENT_MICROMAP_FORMAT_64_TRIANGLES_64_BYTES_NV = 1

sys.modules[__name__] = VkDisplacementMicromapFormatNV

