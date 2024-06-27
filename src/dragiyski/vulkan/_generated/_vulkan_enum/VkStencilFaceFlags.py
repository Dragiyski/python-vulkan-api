from enum import IntFlag

class VkStencilFaceFlags(IntFlag):
    VK_STENCIL_FACE_BACK_BIT = 2
    VK_STENCIL_FACE_FRONT_AND_BACK = 3
    VK_STENCIL_FACE_FRONT_BIT = 1
    VK_STENCIL_FRONT_AND_BACK = VK_STENCIL_FACE_FRONT_AND_BACK