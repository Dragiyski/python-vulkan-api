import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkHeadlessSurfaceCreateFlagsEXT(VulkanUIntFlag):
    pass

sys.modules[__name__] = VkHeadlessSurfaceCreateFlagsEXT
