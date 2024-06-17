import ctypes, sys

class VkPresentRegionsKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPresentRegionsKHR

from . import VkPresentRegionKHR

VkPresentRegionsKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkPresentRegionKHR)),
]
