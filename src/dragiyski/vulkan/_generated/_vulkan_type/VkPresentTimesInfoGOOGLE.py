import ctypes

class VkPresentTimesInfoGOOGLE(ctypes.Structure):
    pass

from .VkPresentTimeGOOGLE import VkPresentTimeGOOGLE

VkPresentTimesInfoGOOGLE._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE)),
]

VkPresentTimesInfoGOOGLE._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchainCount': ctypes.c_uint32,
    'pTimes': ctypes.POINTER(VkPresentTimeGOOGLE),
}
