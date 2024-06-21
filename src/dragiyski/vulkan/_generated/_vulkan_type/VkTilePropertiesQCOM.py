import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkExtent3D import CType as VkExtent3D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('tileSize', VkExtent3D),
    ('apronSize', VkExtent2D),
    ('origin', VkOffset2D),
]
