import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkShaderCodeTypeEXT(VulkanIntEnum):
    VK_SHADER_CODE_TYPE_BINARY_EXT = 0
    VK_SHADER_CODE_TYPE_SPIRV_EXT = 1

sys.modules[__name__] = VkShaderCodeTypeEXT

