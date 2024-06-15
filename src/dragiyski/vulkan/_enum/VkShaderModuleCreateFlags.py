import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkShaderModuleCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkShaderModuleCreateFlags
