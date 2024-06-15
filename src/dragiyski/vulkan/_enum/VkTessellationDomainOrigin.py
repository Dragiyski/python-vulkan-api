import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkTessellationDomainOrigin(VulkanIntEnum):
    VK_TESSELLATION_DOMAIN_ORIGIN_LOWER_LEFT = 1
    VK_TESSELLATION_DOMAIN_ORIGIN_UPPER_LEFT = 0

sys.modules[__name__] = VkTessellationDomainOrigin
