import ctypes, sys

class VkSamplerYcbcrConversionCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkSamplerYcbcrConversionCreateInfo

from . import VkComponentMapping

VkSamplerYcbcrConversionCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('format', ctypes.c_int),
    ('ycbcrModel', ctypes.c_int),
    ('ycbcrRange', ctypes.c_int),
    ('components', VkComponentMapping),
    ('xChromaOffset', ctypes.c_int),
    ('yChromaOffset', ctypes.c_int),
    ('chromaFilter', ctypes.c_int),
    ('forceExplicitReconstruction', ctypes.c_uint32),
]
