import ctypes

class CType(ctypes.Structure):
    pass

from .VkPhysicalDeviceFeatures import CType as VkPhysicalDeviceFeatures

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('features', VkPhysicalDeviceFeatures),
]
