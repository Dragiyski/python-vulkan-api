import ctypes

class VkSparseImageFormatProperties(ctypes.Structure):
    pass

from .VkExtent3D import VkExtent3D

VkSparseImageFormatProperties._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('imageGranularity', VkExtent3D),
    ('flags', ctypes.c_uint32),
]

VkSparseImageFormatProperties._type_ = {
    'aspectMask': ctypes.c_uint32,
    'imageGranularity': VkExtent3D,
    'flags': ctypes.c_uint32,
}
