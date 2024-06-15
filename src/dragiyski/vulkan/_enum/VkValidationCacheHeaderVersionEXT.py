import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkValidationCacheHeaderVersionEXT(VulkanIntEnum):
    VK_VALIDATION_CACHE_HEADER_VERSION_ONE_EXT = 1

sys.modules[__name__] = VkValidationCacheHeaderVersionEXT
