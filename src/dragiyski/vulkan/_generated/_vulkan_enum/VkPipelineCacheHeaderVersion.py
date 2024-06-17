import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkPipelineCacheHeaderVersion(VulkanIntEnum):
    VK_PIPELINE_CACHE_HEADER_VERSION_ONE = 1

sys.modules[__name__] = VkPipelineCacheHeaderVersion

