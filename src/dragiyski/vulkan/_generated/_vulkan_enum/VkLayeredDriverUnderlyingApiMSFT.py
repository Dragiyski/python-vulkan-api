import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkLayeredDriverUnderlyingApiMSFT(VulkanIntEnum):
    VK_LAYERED_DRIVER_UNDERLYING_API_D3D12_MSFT = 1
    VK_LAYERED_DRIVER_UNDERLYING_API_NONE_MSFT = 0

sys.modules[__name__] = VkLayeredDriverUnderlyingApiMSFT

