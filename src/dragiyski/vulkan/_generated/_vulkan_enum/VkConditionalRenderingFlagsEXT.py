import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkConditionalRenderingFlagsEXT(VulkanUIntFlag):
    VK_CONDITIONAL_RENDERING_INVERTED_BIT_EXT = 1

sys.modules[__name__] = VkConditionalRenderingFlagsEXT

