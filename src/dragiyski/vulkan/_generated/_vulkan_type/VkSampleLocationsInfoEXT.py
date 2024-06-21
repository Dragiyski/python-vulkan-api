import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D
from .VkSampleLocationEXT import CType as VkSampleLocationEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsPerPixel', ctypes.c_uint32),
    ('sampleLocationGridSize', VkExtent2D),
    ('sampleLocationsCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkSampleLocationEXT)),
]
