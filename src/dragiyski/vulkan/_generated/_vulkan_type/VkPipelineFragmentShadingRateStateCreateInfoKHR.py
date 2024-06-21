import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentSize', VkExtent2D),
    ('combinerOps', ctypes.ARRAY(ctypes.c_int, 2)),
]
