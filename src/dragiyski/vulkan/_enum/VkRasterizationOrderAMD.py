import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkRasterizationOrderAMD(VulkanIntEnum):
    VK_RASTERIZATION_ORDER_RELAXED_AMD = 1
    VK_RASTERIZATION_ORDER_STRICT_AMD = 0

sys.modules[__name__] = VkRasterizationOrderAMD

