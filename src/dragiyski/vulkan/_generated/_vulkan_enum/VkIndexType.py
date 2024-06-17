import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkIndexType(VulkanIntEnum):
    VK_INDEX_TYPE_NONE_KHR = 1000165000
    VK_INDEX_TYPE_UINT16 = 0
    VK_INDEX_TYPE_UINT32 = 1
    VK_INDEX_TYPE_UINT8_KHR = 1000265000

sys.modules[__name__] = VkIndexType

VkIndexType.VK_INDEX_TYPE_NONE_NV = VkIndexType.VK_INDEX_TYPE_NONE_KHR
VkIndexType.VK_INDEX_TYPE_UINT8_EXT = VkIndexType.VK_INDEX_TYPE_UINT8_KHR
