import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkPipelineCacheValidationVersion(VulkanIntEnum):
    VK_PIPELINE_CACHE_VALIDATION_VERSION_SAFETY_CRITICAL_ONE = 1

sys.modules[__name__] = VkPipelineCacheValidationVersion

