import ctypes

class VkRect2D(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkRect2D._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
]

VkRect2D._type_ = {
    'offset': VkOffset2D,
    'extent': VkExtent2D,
}
