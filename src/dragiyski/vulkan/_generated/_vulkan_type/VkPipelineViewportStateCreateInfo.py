import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D
from .VkViewport import CType as VkViewport

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewports', ctypes.POINTER(VkViewport)),
    ('scissorCount', ctypes.c_uint32),
    ('pScissors', ctypes.POINTER(VkRect2D)),
]
