import ctypes, sys

class VkRect2D(ctypes.Structure):
    pass

sys.modules[__name__] = VkRect2D

from . import VkExtent2D
from . import VkOffset2D

VkRect2D._fields_ = [
    ('offset', VkOffset2D),
    ('extent', VkExtent2D),
]
