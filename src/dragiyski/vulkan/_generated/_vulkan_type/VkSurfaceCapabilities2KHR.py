import ctypes

class CType(ctypes.Structure):
    pass

from .VkSurfaceCapabilitiesKHR import CType as VkSurfaceCapabilitiesKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceCapabilities', VkSurfaceCapabilitiesKHR),
]
