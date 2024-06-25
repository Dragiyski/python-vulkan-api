import ctypes

class VkCoarseSampleOrderCustomNV(ctypes.Structure):
    pass

from .VkCoarseSampleLocationNV import VkCoarseSampleLocationNV

VkCoarseSampleOrderCustomNV._fields_ = [
    ('shadingRate', ctypes.c_int),
    ('sampleCount', ctypes.c_uint32),
    ('sampleLocationCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV)),
]

VkCoarseSampleOrderCustomNV._type_ = {
    'shadingRate': ctypes.c_int,
    'sampleCount': ctypes.c_uint32,
    'sampleLocationCount': ctypes.c_uint32,
    'pSampleLocations': ctypes.POINTER(VkCoarseSampleLocationNV),
}
