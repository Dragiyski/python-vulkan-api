import ctypes, sys

class VkRectLayerKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkRectLayerKHR

from . import VkExtent2D
from . import VkOffset2D

VkRectLayerKHR._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
    ('layer', ctypes.c_uint32),
]