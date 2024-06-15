import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkPipelineDepthStencilStateCreateFlags(VulkanUIntFlag):
    VK_PIPELINE_DEPTH_STENCIL_STATE_CREATE_RASTERIZATION_ORDER_ATTACHMENT_DEPTH_ACCESS_BIT_EXT = 1
    VK_PIPELINE_DEPTH_STENCIL_STATE_CREATE_RASTERIZATION_ORDER_ATTACHMENT_STENCIL_ACCESS_BIT_EXT = 2

sys.modules[__name__] = VkPipelineDepthStencilStateCreateFlags
