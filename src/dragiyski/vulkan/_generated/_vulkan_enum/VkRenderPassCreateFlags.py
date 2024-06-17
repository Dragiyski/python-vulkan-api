import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkRenderPassCreateFlags(VulkanUIntFlag):
    VK_RENDER_PASS_CREATE_TRANSFORM_BIT_QCOM = 2

sys.modules[__name__] = VkRenderPassCreateFlags

