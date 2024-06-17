import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkPipelineMatchControl(VulkanIntEnum):
    VK_PIPELINE_MATCH_CONTROL_APPLICATION_UUID_EXACT_MATCH = 0

sys.modules[__name__] = VkPipelineMatchControl

