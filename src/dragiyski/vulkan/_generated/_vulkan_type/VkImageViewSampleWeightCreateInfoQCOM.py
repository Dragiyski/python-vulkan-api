import ctypes

class VkImageViewSampleWeightCreateInfoQCOM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkImageViewSampleWeightCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('filterCenter', VkOffset2D),
    ('filterSize', VkExtent2D),
    ('numPhases', ctypes.c_uint32),
]

VkImageViewSampleWeightCreateInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'filterCenter': VkOffset2D,
    'filterSize': VkExtent2D,
    'numPhases': ctypes.c_uint32,
}
