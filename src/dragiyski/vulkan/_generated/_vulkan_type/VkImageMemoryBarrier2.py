import ctypes

class VkImageMemoryBarrier2(ctypes.Structure):
    pass

from .VkImageSubresourceRange import VkImageSubresourceRange

VkImageMemoryBarrier2._fields_ = [
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

VkImageMemoryBarrier2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcStageMask': ctypes.c_uint64,
    'srcAccessMask': ctypes.c_uint64,
    'dstStageMask': ctypes.c_uint64,
    'dstAccessMask': ctypes.c_uint64,
    'oldLayout': ctypes.c_int,
    'newLayout': ctypes.c_int,
    'srcQueueFamilyIndex': ctypes.c_uint32,
    'dstQueueFamilyIndex': ctypes.c_uint32,
    'image': ctypes.c_void_p,
    'subresourceRange': VkImageSubresourceRange,
}
