import ctypes, sys
from ..vulkan_base import VulkanIntEnum

class VkVertexInputRate(VulkanIntEnum):
    VK_VERTEX_INPUT_RATE_INSTANCE = 1
    VK_VERTEX_INPUT_RATE_VERTEX = 0

sys.modules[__name__] = VkVertexInputRate

