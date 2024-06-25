import ctypes

class VkSampleLocationsInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'sampleLocationsPerPixel': ctypes.c_uint32,
            'sampleLocationGridSize': VkExtent2D,
            'sampleLocationsCount': ctypes.c_uint32,
            'pSampleLocations': ctypes.POINTER(VkSampleLocationEXT),
        }


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
