import ctypes, sys
from .._vulkan_base import VulkanUIntFlag

class VkStencilFaceFlags(VulkanUIntFlag):
    VK_STENCIL_FACE_FRONT_BIT = 1
    VK_STENCIL_FACE_FRONT_AND_BACK = 3
    VK_STENCIL_FACE_BACK_BIT = 2

sys.modules[__name__] = VkStencilFaceFlags
