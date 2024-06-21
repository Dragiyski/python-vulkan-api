import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('imageGranularity', VkExtent3D),
    ('flags', ctypes.c_uint32),
]
