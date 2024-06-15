import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkInternalAllocationType(VulkanIntEnum):
    VK_INTERNAL_ALLOCATION_TYPE_EXECUTABLE = 0

sys.modules[__name__] = VkInternalAllocationType

