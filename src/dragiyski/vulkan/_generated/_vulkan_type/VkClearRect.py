import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('rect', VkRect2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
]
