import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkDirectDriverLoadingFlagsLUNARG(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkDirectDriverLoadingFlagsLUNARG

