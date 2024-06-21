import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcRect', VkRect2D),
    ('dstRect', VkRect2D),
    ('persistent', ctypes.c_uint32),
]
