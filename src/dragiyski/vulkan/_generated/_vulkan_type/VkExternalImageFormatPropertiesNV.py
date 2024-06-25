import ctypes

class VkExternalImageFormatPropertiesNV(ctypes.Structure):
    pass

from .VkImageFormatProperties import VkImageFormatProperties

VkExternalImageFormatPropertiesNV._fields_ = [
    ('imageFormatProperties', VkImageFormatProperties),
    ('externalMemoryFeatures', ctypes.c_uint32),
    ('exportFromImportedHandleTypes', ctypes.c_uint32),
    ('compatibleHandleTypes', ctypes.c_uint32),
]

VkExternalImageFormatPropertiesNV._type_ = {
    'imageFormatProperties': VkImageFormatProperties,
    'externalMemoryFeatures': ctypes.c_uint32,
    'exportFromImportedHandleTypes': ctypes.c_uint32,
    'compatibleHandleTypes': ctypes.c_uint32,
}
