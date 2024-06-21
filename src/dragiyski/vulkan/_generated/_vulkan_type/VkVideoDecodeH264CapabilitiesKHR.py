import ctypes

class CType(ctypes.Structure):
    pass

from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxLevelIdc', ctypes.c_int),
    ('fieldOffsetGranularity', VkOffset2D),
]
