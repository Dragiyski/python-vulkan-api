import ctypes, sys
from ..vulkan_base import VulkanUIntFlag

class VkStencilFaceFlags(VulkanUIntFlag):
    VK_STENCIL_FACE_BACK_BIT = 2
    VK_STENCIL_FACE_FRONT_AND_BACK = 3
    VK_STENCIL_FACE_FRONT_BIT = 1

sys.modules[__name__] = VkStencilFaceFlags

VkStencilFaceFlags.VK_STENCIL_FRONT_AND_BACK = VkStencilFaceFlags.VK_STENCIL_FACE_FRONT_AND_BACK
