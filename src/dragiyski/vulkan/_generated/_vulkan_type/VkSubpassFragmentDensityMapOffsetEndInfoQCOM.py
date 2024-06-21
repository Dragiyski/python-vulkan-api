import ctypes

class CType(ctypes.Structure):
    pass

from .VkOffset2D import CType as VkOffset2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetCount', ctypes.c_uint32),
    ('pFragmentDensityOffsets', ctypes.POINTER(VkOffset2D)),
]
