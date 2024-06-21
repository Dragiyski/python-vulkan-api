import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D

CType._fields_ = [
    ('maxExtent', VkExtent3D),
    ('maxMipLevels', ctypes.c_uint32),
    ('maxArrayLayers', ctypes.c_uint32),
    ('sampleCounts', ctypes.c_uint32),
    ('maxResourceSize', ctypes.c_uint64),
]
