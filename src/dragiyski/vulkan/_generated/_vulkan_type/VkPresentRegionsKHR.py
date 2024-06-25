import ctypes

class VkPresentRegionsKHR(ctypes.Structure):
    pass

from .VkPresentRegionKHR import VkPresentRegionKHR

VkPresentRegionsKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pRegions', ctypes.POINTER(VkPresentRegionKHR)),
]

VkPresentRegionsKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchainCount': ctypes.c_uint32,
    'pRegions': ctypes.POINTER(VkPresentRegionKHR),
}
