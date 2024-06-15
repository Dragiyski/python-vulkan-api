import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkSurfaceCounterFlagsEXT(VulkanUIntFlag):
    VK_SURFACE_COUNTER_VBLANK_BIT_EXT = 1

sys.modules[__name__] = VkSurfaceCounterFlagsEXT
