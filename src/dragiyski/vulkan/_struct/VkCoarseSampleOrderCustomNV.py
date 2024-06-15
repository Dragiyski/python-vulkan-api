import ctypes, sys

class VkCoarseSampleOrderCustomNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkCoarseSampleOrderCustomNV

from . import VkCoarseSampleLocationNV

VkCoarseSampleOrderCustomNV._fields_ = [
    ('shadingRate', ctypes.c_int),
    ('sampleCount', ctypes.c_uint32),
    ('sampleLocationCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkCoarseSampleLocationNV)),
]
