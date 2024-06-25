import ctypes

class VkSampleLocationsInfoEXT(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D
from .VkSampleLocationEXT import VkSampleLocationEXT

VkSampleLocationsInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleLocationsPerPixel', ctypes.c_uint32),
    ('sampleLocationGridSize', VkExtent2D),
    ('sampleLocationsCount', ctypes.c_uint32),
    ('pSampleLocations', ctypes.POINTER(VkSampleLocationEXT)),
]

VkSampleLocationsInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sampleLocationsPerPixel': ctypes.c_uint32,
    'sampleLocationGridSize': VkExtent2D,
    'sampleLocationsCount': ctypes.c_uint32,
    'pSampleLocations': ctypes.POINTER(VkSampleLocationEXT),
}
