import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineMultisampleStateCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkPipelineMultisampleStateCreateFlags
