import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineLayoutCreateFlags(VulkanUIntFlag):
    VK_PIPELINE_LAYOUT_CREATE_INDEPENDENT_SETS_BIT_EXT = 2

sys.modules[__name__] = VkPipelineLayoutCreateFlags
