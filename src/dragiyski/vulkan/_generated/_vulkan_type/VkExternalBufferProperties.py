import ctypes

class CType(ctypes.Structure):
    pass

from .VkExternalMemoryProperties import CType as VkExternalMemoryProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]
