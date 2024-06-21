import ctypes

class CType(ctypes.Structure):
    pass

from .VkDisplayPlaneCapabilitiesKHR import CType as VkDisplayPlaneCapabilitiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('capabilities', VkDisplayPlaneCapabilitiesKHR),
]
