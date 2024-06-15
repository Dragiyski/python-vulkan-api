import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkAccelerationStructureCompatibilityKHR(VulkanIntEnum):
    VK_ACCELERATION_STRUCTURE_COMPATIBILITY_COMPATIBLE_KHR = 0
    VK_ACCELERATION_STRUCTURE_COMPATIBILITY_INCOMPATIBLE_KHR = 1

sys.modules[__name__] = VkAccelerationStructureCompatibilityKHR
