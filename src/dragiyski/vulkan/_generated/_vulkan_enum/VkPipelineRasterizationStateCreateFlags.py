import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkPipelineRasterizationStateCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkPipelineRasterizationStateCreateFlags

