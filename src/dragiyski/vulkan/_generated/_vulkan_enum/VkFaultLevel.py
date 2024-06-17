import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkFaultLevel(VulkanIntEnum):
    VK_FAULT_LEVEL_CRITICAL = 1
    VK_FAULT_LEVEL_RECOVERABLE = 2
    VK_FAULT_LEVEL_UNASSIGNED = 0
    VK_FAULT_LEVEL_WARNING = 3

sys.modules[__name__] = VkFaultLevel

