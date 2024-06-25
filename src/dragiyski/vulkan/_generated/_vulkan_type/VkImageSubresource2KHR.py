import ctypes

class VkImageSubresource2KHR(ctypes.Structure):
    pass

from .VkImageSubresource import VkImageSubresource

VkImageSubresource2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageSubresource', VkImageSubresource),
]

VkImageSubresource2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageSubresource': VkImageSubresource,
}
