import ctypes

class VkRectLayerKHR(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkRectLayerKHR._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
    ('layer', ctypes.c_uint32),
]

VkRectLayerKHR._type_ = {
    'offset': VkOffset2D,
    'extent': VkExtent2D,
    'layer': ctypes.c_uint32,
}
