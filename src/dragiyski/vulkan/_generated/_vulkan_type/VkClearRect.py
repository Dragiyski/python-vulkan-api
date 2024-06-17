import ctypes, sys

class VkClearRect(ctypes.Structure):
    pass

sys.modules[__name__] = VkClearRect

from . import VkRect2D

VkClearRect._fields_ = [
    ('rect', VkRect2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
]
