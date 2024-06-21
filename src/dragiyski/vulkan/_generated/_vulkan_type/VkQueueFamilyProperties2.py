import ctypes

class CType(ctypes.Structure):
    pass

from .VkQueueFamilyProperties import CType as VkQueueFamilyProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyProperties', VkQueueFamilyProperties),
]
