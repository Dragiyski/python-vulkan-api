import ctypes, sys

class VkPipelineDiscardRectangleStateCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineDiscardRectangleStateCreateInfoEXT

from . import VkRect2D

VkPipelineDiscardRectangleStateCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('discardRectangleMode', ctypes.c_int),
    ('discardRectangleCount', ctypes.c_uint32),
    ('pDiscardRectangles', ctypes.POINTER(VkRect2D)),
]
