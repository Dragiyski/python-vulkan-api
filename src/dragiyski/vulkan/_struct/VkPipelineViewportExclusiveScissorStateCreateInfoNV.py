import ctypes, sys

class VkPipelineViewportExclusiveScissorStateCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineViewportExclusiveScissorStateCreateInfoNV

from . import VkRect2D

VkPipelineViewportExclusiveScissorStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('exclusiveScissorCount', ctypes.c_uint32),
    ('pExclusiveScissors', ctypes.POINTER(VkRect2D)),
]
