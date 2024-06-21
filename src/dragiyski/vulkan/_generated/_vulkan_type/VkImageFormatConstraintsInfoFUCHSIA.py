import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCreateInfo import CType as VkImageCreateInfo
from .VkSysmemColorSpaceFUCHSIA import CType as VkSysmemColorSpaceFUCHSIA

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageCreateInfo', VkImageCreateInfo),
    ('requiredFormatFeatures', ctypes.c_uint32),
    ('flags', ctypes.c_uint32),
    ('sysmemPixelFormat', ctypes.c_uint64),
    ('colorSpaceCount', ctypes.c_uint32),
    ('pColorSpaces', ctypes.POINTER(VkSysmemColorSpaceFUCHSIA)),
]
