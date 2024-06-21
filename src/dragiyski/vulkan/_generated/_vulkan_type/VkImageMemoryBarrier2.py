import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresourceRange import CType as VkImageSubresourceRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcStageMask', ctypes.c_uint64),
    ('srcAccessMask', ctypes.c_uint64),
    ('dstStageMask', ctypes.c_uint64),
    ('dstAccessMask', ctypes.c_uint64),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('srcQueueFamilyIndex', ctypes.c_uint32),
    ('dstQueueFamilyIndex', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('subresourceRange', VkImageSubresourceRange),
]
