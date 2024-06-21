import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayPropertiesKHR import CType as VkDisplayPropertiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayProperties', VkDisplayPropertiesKHR),
]
