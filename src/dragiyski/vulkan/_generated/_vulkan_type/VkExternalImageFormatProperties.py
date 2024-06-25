import ctypes

class VkExternalImageFormatProperties(ctypes.Structure):
    pass

from .VkExternalMemoryProperties import VkExternalMemoryProperties

VkExternalImageFormatProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]

VkExternalImageFormatProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'externalMemoryProperties': VkExternalMemoryProperties,
}
