import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineColorBlendStateCreateFlags(VulkanUIntFlag):
    VK_PIPELINE_COLOR_BLEND_STATE_CREATE_RASTERIZATION_ORDER_ATTACHMENT_ACCESS_BIT_EXT = 1

sys.modules[__name__] = VkPipelineColorBlendStateCreateFlags
