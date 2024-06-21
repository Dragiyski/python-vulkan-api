import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('discardRectangleMode', ctypes.c_int),
    ('discardRectangleCount', ctypes.c_uint32),
    ('pDiscardRectangles', ctypes.POINTER(VkRect2D)),
]
