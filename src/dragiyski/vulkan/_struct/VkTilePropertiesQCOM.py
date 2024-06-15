import ctypes, sys

class VkTilePropertiesQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkTilePropertiesQCOM

from . import VkExtent3D
from . import VkExtent2D
from . import VkOffset2D

VkTilePropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('tileSize', VkExtent3D),
    ('apronSize', VkExtent2D),
    ('origin', VkOffset2D),
]
