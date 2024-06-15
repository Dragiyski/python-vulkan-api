import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkBuildAccelerationStructureModeKHR(VulkanIntEnum):
    VK_BUILD_ACCELERATION_STRUCTURE_MODE_UPDATE_KHR = 1
    VK_BUILD_ACCELERATION_STRUCTURE_MODE_BUILD_KHR = 0

sys.modules[__name__] = VkBuildAccelerationStructureModeKHR
