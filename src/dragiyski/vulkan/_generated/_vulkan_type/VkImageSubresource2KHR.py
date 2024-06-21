import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresource import CType as VkImageSubresource

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageSubresource', VkImageSubresource),
]
