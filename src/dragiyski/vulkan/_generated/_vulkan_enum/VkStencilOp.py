from enum import IntEnum

class VkStencilOp(IntEnum):
    VK_STENCIL_OP_DECREMENT_AND_CLAMP = 4
    VK_STENCIL_OP_DECREMENT_AND_WRAP = 7
    VK_STENCIL_OP_INCREMENT_AND_CLAMP = 3
    VK_STENCIL_OP_INCREMENT_AND_WRAP = 6
    VK_STENCIL_OP_INVERT = 5
    VK_STENCIL_OP_KEEP = 0
    VK_STENCIL_OP_REPLACE = 2
    VK_STENCIL_OP_ZERO = 1
