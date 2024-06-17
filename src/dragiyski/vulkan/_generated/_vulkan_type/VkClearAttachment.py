import ctypes, sys

class VkClearAttachment(ctypes.Structure):
    pass

sys.modules[__name__] = VkClearAttachment

from . import VkClearValue

VkClearAttachment._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('colorAttachment', ctypes.c_uint32),
    ('clearValue', VkClearValue),
]
