import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearValue import CType as VkClearValue
from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('renderPass', ctypes.c_void_p),
    ('framebuffer', ctypes.c_void_p),
    ('renderArea', VkRect2D),
    ('clearValueCount', ctypes.c_uint32),
    ('pClearValues', ctypes.POINTER(VkClearValue)),
]
