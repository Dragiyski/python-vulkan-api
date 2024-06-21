import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayPlanePropertiesKHR import CType as VkDisplayPlanePropertiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPlaneProperties', VkDisplayPlanePropertiesKHR),
]
