import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayModePropertiesKHR import CType as VkDisplayModePropertiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayModeProperties', VkDisplayModePropertiesKHR),
]
