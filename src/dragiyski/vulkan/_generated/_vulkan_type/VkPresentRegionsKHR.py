import ctypes

class CType(ctypes.Structure):
    pass

from .VkPresentRegionKHR import CType as VkPresentRegionKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkPresentRegionKHR)),
]
