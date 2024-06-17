import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkPipelineDynamicStateCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkPipelineDynamicStateCreateFlags

