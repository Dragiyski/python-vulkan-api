import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkShaderModuleCreateFlags(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkShaderModuleCreateFlags

