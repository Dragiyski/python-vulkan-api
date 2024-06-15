import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkCopyAccelerationStructureModeKHR(VulkanIntEnum):
    VK_COPY_ACCELERATION_STRUCTURE_MODE_SERIALIZE_KHR = 2
    VK_COPY_ACCELERATION_STRUCTURE_MODE_DESERIALIZE_KHR = 3
    VK_COPY_ACCELERATION_STRUCTURE_MODE_CLONE_KHR = 0
    VK_COPY_ACCELERATION_STRUCTURE_MODE_COMPACT_KHR = 1

sys.modules[__name__] = VkCopyAccelerationStructureModeKHR
