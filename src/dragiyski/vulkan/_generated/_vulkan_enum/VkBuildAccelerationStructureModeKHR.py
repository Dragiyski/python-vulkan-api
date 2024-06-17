import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkBuildAccelerationStructureModeKHR(VulkanIntEnum):
    VK_BUILD_ACCELERATION_STRUCTURE_MODE_BUILD_KHR = 0
    VK_BUILD_ACCELERATION_STRUCTURE_MODE_UPDATE_KHR = 1

sys.modules[__name__] = VkBuildAccelerationStructureModeKHR

