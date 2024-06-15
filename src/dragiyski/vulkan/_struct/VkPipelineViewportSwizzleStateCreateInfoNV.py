import ctypes, sys

class VkPipelineViewportSwizzleStateCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineViewportSwizzleStateCreateInfoNV

from . import VkViewportSwizzleNV

VkPipelineViewportSwizzleStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportSwizzles', ctypes.POINTER(VkViewportSwizzleNV)),
]
