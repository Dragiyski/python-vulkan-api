import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkAccelerationStructureBuildTypeKHR(VulkanIntEnum):
    VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_KHR = 0
    VK_ACCELERATION_STRUCTURE_BUILD_TYPE_HOST_OR_DEVICE_KHR = 2
    VK_ACCELERATION_STRUCTURE_BUILD_TYPE_DEVICE_KHR = 1

sys.modules[__name__] = VkAccelerationStructureBuildTypeKHR
