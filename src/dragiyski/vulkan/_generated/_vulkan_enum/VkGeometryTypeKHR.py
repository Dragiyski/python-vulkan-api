import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkGeometryTypeKHR(VulkanIntEnum):
    VK_GEOMETRY_TYPE_AABBS_KHR = 1
    VK_GEOMETRY_TYPE_INSTANCES_KHR = 2
    VK_GEOMETRY_TYPE_TRIANGLES_KHR = 0

sys.modules[__name__] = VkGeometryTypeKHR

VkGeometryTypeKHR.VK_GEOMETRY_TYPE_AABBS_NV = VkGeometryTypeKHR.VK_GEOMETRY_TYPE_AABBS_KHR
VkGeometryTypeKHR.VK_GEOMETRY_TYPE_TRIANGLES_NV = VkGeometryTypeKHR.VK_GEOMETRY_TYPE_TRIANGLES_KHR
