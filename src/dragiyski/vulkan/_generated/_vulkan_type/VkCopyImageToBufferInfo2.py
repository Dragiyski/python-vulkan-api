import ctypes

class VkCopyImageToBufferInfo2(ctypes.Structure):
    pass

from .VkBufferImageCopy2 import VkBufferImageCopy2

VkCopyImageToBufferInfo2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcImage', ctypes.c_void_p),
    ('srcImageLayout', ctypes.c_int),
    ('dstBuffer', ctypes.c_void_p),
    ('regionCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkBufferImageCopy2)),
]

VkCopyImageToBufferInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcImage': ctypes.c_void_p,
    'srcImageLayout': ctypes.c_int,
    'dstBuffer': ctypes.c_void_p,
    'regionCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkBufferImageCopy2),
}
