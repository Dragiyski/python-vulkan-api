import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkRayTracingInvocationReorderModeNV(VulkanIntEnum):
    VK_RAY_TRACING_INVOCATION_REORDER_MODE_NONE_NV = 0
    VK_RAY_TRACING_INVOCATION_REORDER_MODE_REORDER_NV = 1

sys.modules[__name__] = VkRayTracingInvocationReorderModeNV

