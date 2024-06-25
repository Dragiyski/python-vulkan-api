import ctypes

class VkBufferCollectionPropertiesFUCHSIA(ctypes.Structure):
    pass

from .VkComponentMapping import VkComponentMapping
from .VkSysmemColorSpaceFUCHSIA import VkSysmemColorSpaceFUCHSIA

VkBufferCollectionPropertiesFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryTypeBits', ctypes.c_uint32),
    ('bufferCount', ctypes.c_uint32),
    ('createInfoIndex', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('formatFeatures', ctypes.c_uint32),
    ('sysmemColorSpaceIndex', VkSysmemColorSpaceFUCHSIA),
    ('samplerYcbcrConversionComponents', VkComponentMapping),
    ('suggestedYcbcrModel', ctypes.c_int),
    ('suggestedYcbcrRange', ctypes.c_int),
    ('suggestedXChromaOffset', ctypes.c_int),
    ('suggestedYChromaOffset', ctypes.c_int),
]

VkBufferCollectionPropertiesFUCHSIA._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryTypeBits': ctypes.c_uint32,
    'bufferCount': ctypes.c_uint32,
    'createInfoIndex': ctypes.c_uint32,
    'sysmemPixelFormat': ctypes.c_uint64,
    'formatFeatures': ctypes.c_uint32,
    'sysmemColorSpaceIndex': VkSysmemColorSpaceFUCHSIA,
    'samplerYcbcrConversionComponents': VkComponentMapping,
    'suggestedYcbcrModel': ctypes.c_int,
    'suggestedYcbcrRange': ctypes.c_int,
    'suggestedXChromaOffset': ctypes.c_int,
    'suggestedYChromaOffset': ctypes.c_int,
}
