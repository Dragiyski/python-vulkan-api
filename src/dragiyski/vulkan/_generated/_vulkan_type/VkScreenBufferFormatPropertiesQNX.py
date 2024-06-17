import ctypes, sys

class VkScreenBufferFormatPropertiesQNX(ctypes.Structure):
    pass

sys.modules[__name__] = VkScreenBufferFormatPropertiesQNX

from . import VkComponentMapping

VkScreenBufferFormatPropertiesQNX._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('externalFormat', ctypes.c_uint64),
    ('screenUsage', ctypes.c_uint64),
    ('formatFeatures', ctypes.c_uint32),
    ('samplerYcbcrConversionComponents', VkComponentMapping),
    ('suggestedYcbcrModel', ctypes.c_int),
    ('suggestedYcbcrRange', ctypes.c_int),
    ('suggestedXChromaOffset', ctypes.c_int),
    ('suggestedYChromaOffset', ctypes.c_int),
]
