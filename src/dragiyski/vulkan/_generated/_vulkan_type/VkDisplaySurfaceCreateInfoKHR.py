import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('displayMode', ctypes.c_void_p),
    ('planeIndex', ctypes.c_uint32),
    ('planeStackIndex', ctypes.c_uint32),
    ('transform', ctypes.c_uint32),
    ('globalAlpha', ctypes.c_float),
    ('alphaMode', ctypes.c_uint32),
    ('imageExtent', VkExtent2D),
]
