import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkShaderCorePropertiesFlagsAMD(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkShaderCorePropertiesFlagsAMD

