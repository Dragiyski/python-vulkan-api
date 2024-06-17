import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkShaderInfoTypeAMD(VulkanIntEnum):
    VK_SHADER_INFO_TYPE_BINARY_AMD = 1
    VK_SHADER_INFO_TYPE_DISASSEMBLY_AMD = 2
    VK_SHADER_INFO_TYPE_STATISTICS_AMD = 0

sys.modules[__name__] = VkShaderInfoTypeAMD

