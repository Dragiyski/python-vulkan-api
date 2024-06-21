import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('visibleRegion', VkExtent2D),
    ('refreshRate', ctypes.c_uint32),
]
