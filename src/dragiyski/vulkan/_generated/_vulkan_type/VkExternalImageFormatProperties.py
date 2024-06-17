import ctypes, sys

class VkExternalImageFormatProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkExternalImageFormatProperties

from . import VkExternalMemoryProperties

VkExternalImageFormatProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]
