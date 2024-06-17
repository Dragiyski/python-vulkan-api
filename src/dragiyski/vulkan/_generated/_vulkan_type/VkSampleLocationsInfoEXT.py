import ctypes, sys

class VkSampleLocationsInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkSampleLocationsInfoEXT

from . import VkExtent2D
from . import VkSampleLocationEXT

VkSampleLocationsInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsPerPixel', ctypes.c_uint32),
    ('sampleLocationGridSize', VkExtent2D),
    ('sampleLocationsCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkSampleLocationEXT)),
]
