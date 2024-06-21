import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageFormatProperties import CType as VkImageFormatProperties

CType._fields_ = [
    ('imageFormatProperties', VkImageFormatProperties),
    ('externalMemoryFeatures', ctypes.c_uint32),
    ('exportFromImportedHandleTypes', ctypes.c_uint32),
    ('compatibleHandleTypes', ctypes.c_uint32),
]
