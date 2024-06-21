import ctypes

class CType(ctypes.Structure):
    pass

from .VkSubresourceLayout import CType as VkSubresourceLayout

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('subresourceLayout', VkSubresourceLayout),
]
