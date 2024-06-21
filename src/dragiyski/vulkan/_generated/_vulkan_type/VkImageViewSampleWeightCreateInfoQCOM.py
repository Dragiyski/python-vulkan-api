import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('filterCenter', VkOffset2D),
    ('filterSize', VkExtent2D),
    ('numPhases', ctypes.c_uint32),
]
