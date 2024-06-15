import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkSystemAllocationScope(VulkanIntEnum):
    VK_SYSTEM_ALLOCATION_SCOPE_CACHE = 2
    VK_SYSTEM_ALLOCATION_SCOPE_COMMAND = 0
    VK_SYSTEM_ALLOCATION_SCOPE_DEVICE = 3
    VK_SYSTEM_ALLOCATION_SCOPE_INSTANCE = 4
    VK_SYSTEM_ALLOCATION_SCOPE_OBJECT = 1

sys.modules[__name__] = VkSystemAllocationScope

