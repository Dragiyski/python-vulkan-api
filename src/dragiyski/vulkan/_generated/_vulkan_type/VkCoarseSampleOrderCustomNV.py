import ctypes

class CType(ctypes.Structure):
    pass

from .VkCoarseSampleLocationNV import CType as VkCoarseSampleLocationNV

CType._fields_ = [
    ('shadingRate', ctypes.c_int),
    ('sampleCount', ctypes.c_uint32),
    ('sampleLocationCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV)),
]
