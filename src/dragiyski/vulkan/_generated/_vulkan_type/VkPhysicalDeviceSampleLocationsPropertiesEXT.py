import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationSampleCounts', ctypes.c_uint32),
    ('maxSampleLocationGridSize', VkExtent2D),
    ('sampleLocationCoordinateRange', ctypes.ARRAY(ctypes.c_float, 2)),
    ('sampleLocationSubPixelBits', ctypes.c_uint32),
    ('variableSampleLocations', ctypes.c_uint32),
]
