import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping
from .VkImageSubresourceRange import CType as VkImageSubresourceRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('viewType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('components', VkComponentMapping),
    ('subresourceRange', VkImageSubresourceRange),
]
