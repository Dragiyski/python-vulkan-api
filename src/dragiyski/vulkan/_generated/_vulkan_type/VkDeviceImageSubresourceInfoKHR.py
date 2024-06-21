import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCreateInfo import CType as VkImageCreateInfo
from .VkImageSubresource2KHR import CType as VkImageSubresource2KHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('pSubresource', ctypes.POINTER(VkImageSubresource2KHR)),
]
