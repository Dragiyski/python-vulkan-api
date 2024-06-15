import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkAccelerationStructureMemoryRequirementsTypeNV(VulkanIntEnum):
    VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_UPDATE_SCRATCH_NV = 2
    VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_BUILD_SCRATCH_NV = 1
    VK_ACCELERATION_STRUCTURE_MEMORY_REQUIREMENTS_TYPE_OBJECT_NV = 0

sys.modules[__name__] = VkAccelerationStructureMemoryRequirementsTypeNV
