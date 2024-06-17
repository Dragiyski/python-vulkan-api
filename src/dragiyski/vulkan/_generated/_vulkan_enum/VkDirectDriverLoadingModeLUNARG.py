import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkDirectDriverLoadingModeLUNARG(VulkanIntEnum):
    VK_DIRECT_DRIVER_LOADING_MODE_EXCLUSIVE_LUNARG = 0
    VK_DIRECT_DRIVER_LOADING_MODE_INCLUSIVE_LUNARG = 1

sys.modules[__name__] = VkDirectDriverLoadingModeLUNARG

