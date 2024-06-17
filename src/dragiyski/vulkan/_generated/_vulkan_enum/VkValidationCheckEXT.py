import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkValidationCheckEXT(VulkanIntEnum):
    VK_VALIDATION_CHECK_ALL_EXT = 0
    VK_VALIDATION_CHECK_SHADERS_EXT = 1

sys.modules[__name__] = VkValidationCheckEXT

