import ctypes, sys

class VkImageViewSampleWeightCreateInfoQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageViewSampleWeightCreateInfoQCOM

from . import VkOffset2D
from . import VkExtent2D

VkImageViewSampleWeightCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('filterCenter', VkOffset2D),
    ('filterSize', VkExtent2D),
    ('numPhases', ctypes.c_uint32),
]
