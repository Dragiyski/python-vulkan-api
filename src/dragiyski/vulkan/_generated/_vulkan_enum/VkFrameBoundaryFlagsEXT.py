import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkFrameBoundaryFlagsEXT(VulkanUIntFlag):
    VK_FRAME_BOUNDARY_FRAME_END_BIT_EXT = 1

sys.modules[__name__] = VkFrameBoundaryFlagsEXT

