import ctypes

class CType(ctypes.Structure):
    pass

from .VkPhysicalDeviceProperties import CType as VkPhysicalDeviceProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkPhysicalDeviceProperties),
]
