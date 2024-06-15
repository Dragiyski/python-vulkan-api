import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkDirectDriverLoadingFlagsLUNARG(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkDirectDriverLoadingFlagsLUNARG
