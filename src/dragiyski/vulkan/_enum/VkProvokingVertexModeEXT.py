import ctypes, sys
from .._vulkan_base import VulkanIntEnum

class VkProvokingVertexModeEXT(VulkanIntEnum):
    VK_PROVOKING_VERTEX_MODE_LAST_VERTEX_EXT = 1
    VK_PROVOKING_VERTEX_MODE_FIRST_VERTEX_EXT = 0

sys.modules[__name__] = VkProvokingVertexModeEXT
