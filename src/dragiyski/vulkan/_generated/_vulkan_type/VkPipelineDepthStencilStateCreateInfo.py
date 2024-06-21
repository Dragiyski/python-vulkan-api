import ctypes

class CType(ctypes.Structure):
    pass

from .VkStencilOpState import CType as VkStencilOpState

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('depthTestEnable', ctypes.c_uint32),
    ('depthWriteEnable', ctypes.c_uint32),
    ('depthCompareOp', ctypes.c_int),
    ('depthBoundsTestEnable', ctypes.c_uint32),
    ('stencilTestEnable', ctypes.c_uint32),
    ('front', VkStencilOpState),
    ('back', VkStencilOpState),
    ('minDepthBounds', ctypes.c_float),
    ('maxDepthBounds', ctypes.c_float),
]
