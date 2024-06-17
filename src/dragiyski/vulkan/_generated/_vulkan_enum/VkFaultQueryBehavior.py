import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkFaultQueryBehavior(VulkanIntEnum):
    VK_FAULT_QUERY_BEHAVIOR_GET_AND_CLEAR_ALL_FAULTS = 0

sys.modules[__name__] = VkFaultQueryBehavior

