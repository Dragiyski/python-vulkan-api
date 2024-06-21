import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearValue import CType as VkClearValue

CType._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('colorAttachment', ctypes.c_uint32),
    ('clearValue', VkClearValue),
]
