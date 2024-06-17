import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkAccelerationStructureMotionInstanceTypeNV(VulkanIntEnum):
    VK_ACCELERATION_STRUCTURE_MOTION_INSTANCE_TYPE_MATRIX_MOTION_NV = 1
    VK_ACCELERATION_STRUCTURE_MOTION_INSTANCE_TYPE_SRT_MOTION_NV = 2
    VK_ACCELERATION_STRUCTURE_MOTION_INSTANCE_TYPE_STATIC_NV = 0

sys.modules[__name__] = VkAccelerationStructureMotionInstanceTypeNV

