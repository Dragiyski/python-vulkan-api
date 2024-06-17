import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkPipelineCompilerControlFlagsAMD(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkPipelineCompilerControlFlagsAMD

