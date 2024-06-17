import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkOutOfBandQueueTypeNV(VulkanIntEnum):
    VK_OUT_OF_BAND_QUEUE_TYPE_PRESENT_NV = 1
    VK_OUT_OF_BAND_QUEUE_TYPE_RENDER_NV = 0

sys.modules[__name__] = VkOutOfBandQueueTypeNV

