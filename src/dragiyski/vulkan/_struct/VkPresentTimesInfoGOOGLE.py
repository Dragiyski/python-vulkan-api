import ctypes, sys

class VkPresentTimesInfoGOOGLE(ctypes.Structure):
    pass

sys.modules[__name__] = VkPresentTimesInfoGOOGLE

from . import VkPresentTimeGOOGLE

VkPresentTimesInfoGOOGLE._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE)),
]
