import ctypes

class VkCopyBufferToImageInfo2(ctypes.Structure):
    pass

from .VkBufferImageCopy2 import VkBufferImageCopy2

VkCopyBufferToImageInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcBuffer', ctypes.c_void_p),
    ('dstImage', ctypes.c_void_p),
    ('dstImageLayout', ctypes.c_int),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferImageCopy2)),
]

VkCopyBufferToImageInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcBuffer': ctypes.c_void_p,
    'dstImage': ctypes.c_void_p,
    'dstImageLayout': ctypes.c_int,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkBufferImageCopy2),
}
