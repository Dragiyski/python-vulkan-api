import ctypes

class VkImageMemoryBarrier(ctypes.Structure):
    pass

from .VkImageSubresourceRange import VkImageSubresourceRange

VkImageMemoryBarrier._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcAccessMask', ctypes.c_uint32),
    ('dstAccessMask', ctypes.c_uint32),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('srcQueueFamilyIndex', ctypes.c_uint32),
    ('dstQueueFamilyIndex', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('subresourceRange', VkImageSubresourceRange),
]

VkImageMemoryBarrier._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'srcAccessMask': ctypes.c_uint32,
    'dstAccessMask': ctypes.c_uint32,
    'oldLayout': ctypes.c_int,
    'newLayout': ctypes.c_int,
    'srcQueueFamilyIndex': ctypes.c_uint32,
    'dstQueueFamilyIndex': ctypes.c_uint32,
    'image': ctypes.c_void_p,
    'subresourceRange': VkImageSubresourceRange,
}
