import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkAccelerationStructureTypeKHR(VulkanIntEnum):
    VK_ACCELERATION_STRUCTURE_TYPE_TOP_LEVEL_KHR = 0
    VK_ACCELERATION_STRUCTURE_TYPE_GENERIC_KHR = 2
    VK_ACCELERATION_STRUCTURE_TYPE_BOTTOM_LEVEL_KHR = 1

sys.modules[__name__] = VkAccelerationStructureTypeKHR
