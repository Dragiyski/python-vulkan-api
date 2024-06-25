import ctypes

class VkFormatProperties2(ctypes.Structure):
    pass

from .VkFormatProperties import VkFormatProperties

VkFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('formatProperties', VkFormatProperties),
]

VkFormatProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'formatProperties': VkFormatProperties,
}
