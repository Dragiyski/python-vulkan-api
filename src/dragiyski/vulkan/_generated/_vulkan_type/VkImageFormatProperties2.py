import ctypes

class VkImageFormatProperties2(ctypes.Structure):
    pass

from .VkImageFormatProperties import VkImageFormatProperties

VkImageFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageFormatProperties', VkImageFormatProperties),
]

VkImageFormatProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'imageFormatProperties': VkImageFormatProperties,
}
