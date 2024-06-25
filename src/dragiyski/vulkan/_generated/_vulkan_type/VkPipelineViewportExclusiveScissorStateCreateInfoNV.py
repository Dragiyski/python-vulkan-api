import ctypes

class VkPipelineViewportExclusiveScissorStateCreateInfoNV(ctypes.Structure):
    pass

from .VkRect2D import VkRect2D

VkPipelineViewportExclusiveScissorStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('exclusiveScissorCount', ctypes.c_uint32),
    ('pExclusiveScissors', ctypes.POINTER(VkRect2D)),
]

VkPipelineViewportExclusiveScissorStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'exclusiveScissorCount': ctypes.c_uint32,
    'pExclusiveScissors': ctypes.POINTER(VkRect2D),
}
