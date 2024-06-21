import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresourceRange import CType as VkImageSubresourceRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('image', ctypes.c_void_p),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('subresourceRange', VkImageSubresourceRange),
]
