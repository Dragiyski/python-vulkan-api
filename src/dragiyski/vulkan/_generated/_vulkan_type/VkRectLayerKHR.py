import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
    ('layer', ctypes.c_uint32),
]
