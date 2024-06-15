import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkGeometryFlagsKHR(VulkanUIntFlag):
    VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR = 2
    VK_GEOMETRY_OPAQUE_BIT_KHR = 1

sys.modules[__name__] = VkGeometryFlagsKHR

VkGeometryFlagsKHR.VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_NV = VkGeometryFlagsKHR.VK_GEOMETRY_NO_DUPLICATE_ANY_HIT_INVOCATION_BIT_KHR
VkGeometryFlagsKHR.VK_GEOMETRY_OPAQUE_BIT_NV = VkGeometryFlagsKHR.VK_GEOMETRY_OPAQUE_BIT_KHR
