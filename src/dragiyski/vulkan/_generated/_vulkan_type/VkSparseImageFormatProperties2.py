import ctypes

class VkSparseImageFormatProperties2(ctypes.Structure):
    pass

from .VkSparseImageFormatProperties import VkSparseImageFormatProperties

VkSparseImageFormatProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkSparseImageFormatProperties),
]

VkSparseImageFormatProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'properties': VkSparseImageFormatProperties,
}
