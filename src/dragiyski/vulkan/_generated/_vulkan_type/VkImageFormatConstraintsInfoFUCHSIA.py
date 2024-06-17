import ctypes, sys

class VkImageFormatConstraintsInfoFUCHSIA(ctypes.Structure):
    pass

sys.modules[__name__] = VkImageFormatConstraintsInfoFUCHSIA

from . import VkImageCreateInfo
from . import VkSysmemColorSpaceFUCHSIA

VkImageFormatConstraintsInfoFUCHSIA._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageCreateInfo', VkImageCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('colorSpaceCount', ctypes.c_uint32),
    ('pColorSpaces', ctypes.POINTER(VkSysmemColorSpaceFUCHSIA)),
]
