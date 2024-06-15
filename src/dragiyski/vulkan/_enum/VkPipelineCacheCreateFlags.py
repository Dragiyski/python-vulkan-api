import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineCacheCreateFlags(VulkanUIntFlag):
    VK_PIPELINE_CACHE_CREATE_EXTERNALLY_SYNCHRONIZED_BIT = 1

sys.modules[__name__] = VkPipelineCacheCreateFlags
