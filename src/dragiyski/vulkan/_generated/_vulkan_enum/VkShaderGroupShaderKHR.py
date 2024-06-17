import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkShaderGroupShaderKHR(VulkanIntEnum):
    VK_SHADER_GROUP_SHADER_ANY_HIT_KHR = 2
    VK_SHADER_GROUP_SHADER_CLOSEST_HIT_KHR = 1
    VK_SHADER_GROUP_SHADER_GENERAL_KHR = 0
    VK_SHADER_GROUP_SHADER_INTERSECTION_KHR = 3

sys.modules[__name__] = VkShaderGroupShaderKHR

