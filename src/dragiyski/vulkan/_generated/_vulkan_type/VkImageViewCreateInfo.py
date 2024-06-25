import ctypes

class VkImageViewCreateInfo(ctypes.Structure):
    pass

from .VkComponentMapping import VkComponentMapping
from .VkImageSubresourceRange import VkImageSubresourceRange

VkImageViewCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('image', ctypes.c_void_p),
    ('viewType', ctypes.c_int),
    ('format', ctypes.c_int),
    ('components', VkComponentMapping),
    ('subresourceRange', VkImageSubresourceRange),
]

VkImageViewCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'image': ctypes.c_void_p,
    'viewType': ctypes.c_int,
    'format': ctypes.c_int,
    'components': VkComponentMapping,
    'subresourceRange': VkImageSubresourceRange,
}
