import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkGeometryTypeKHR(VulkanIntEnum):
    VK_GEOMETRY_TYPE_AABBS_KHR = 1
    VK_GEOMETRY_TYPE_TRIANGLES_KHR = 0
    VK_GEOMETRY_TYPE_INSTANCES_KHR = 2

sys.modules[__name__] = VkGeometryTypeKHR
