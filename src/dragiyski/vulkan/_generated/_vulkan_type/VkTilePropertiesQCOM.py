import ctypes

class VkTilePropertiesQCOM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D
from .VkExtent3D import VkExtent3D
from .VkOffset2D import VkOffset2D

VkTilePropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('tileSize', VkExtent3D),
    ('apronSize', VkExtent2D),
    ('origin', VkOffset2D),
]

VkTilePropertiesQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'tileSize': VkExtent3D,
    'apronSize': VkExtent2D,
    'origin': VkOffset2D,
}
