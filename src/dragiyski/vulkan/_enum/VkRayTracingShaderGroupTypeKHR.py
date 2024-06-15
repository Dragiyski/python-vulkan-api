import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkRayTracingShaderGroupTypeKHR(VulkanIntEnum):
    VK_RAY_TRACING_SHADER_GROUP_TYPE_PROCEDURAL_HIT_GROUP_KHR = 2
    VK_RAY_TRACING_SHADER_GROUP_TYPE_GENERAL_KHR = 0
    VK_RAY_TRACING_SHADER_GROUP_TYPE_TRIANGLES_HIT_GROUP_KHR = 1

sys.modules[__name__] = VkRayTracingShaderGroupTypeKHR
