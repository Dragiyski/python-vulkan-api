import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkFaultType(VulkanIntEnum):
    VK_FAULT_TYPE_PHYSICAL_DEVICE = 4
    VK_FAULT_TYPE_UNASSIGNED = 1
    VK_FAULT_TYPE_SYSTEM = 3
    VK_FAULT_TYPE_IMPLEMENTATION = 2
    VK_FAULT_TYPE_INVALID = 0
    VK_FAULT_TYPE_COMMAND_BUFFER_FULL = 5
    VK_FAULT_TYPE_INVALID_API_USAGE = 6

sys.modules[__name__] = VkFaultType
