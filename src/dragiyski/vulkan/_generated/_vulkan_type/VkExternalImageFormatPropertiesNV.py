import ctypes, sys

class VkExternalImageFormatPropertiesNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkExternalImageFormatPropertiesNV

from . import VkImageFormatProperties

VkExternalImageFormatPropertiesNV._fields_ = [
    ('imageFormatProperties', VkImageFormatProperties),
    ('externalMemoryFeatures', ctypes.c_uint32),
    ('exportFromImportedHandleTypes', ctypes.c_uint32),
    ('compatibleHandleTypes', ctypes.c_uint32),
]
