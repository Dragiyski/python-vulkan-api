import ctypes

class CType(ctypes.Structure):
    pass

from .VkComponentMapping import CType as VkComponentMapping
from .VkSysmemColorSpaceFUCHSIA import CType as VkSysmemColorSpaceFUCHSIA

CType._fields_ = [
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
