import ctypes

class VkCopyImageInfo2(ctypes.Structure):
    pass

from .VkImageCopy2 import VkImageCopy2

VkCopyImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkImageCopy2)),
]

VkCopyImageInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcImage': ctypes.c_void_p,
    'srcImageLayout': ctypes.c_int,
    'dstImage': ctypes.c_void_p,
    'dstImageLayout': ctypes.c_int,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkImageCopy2),
}
