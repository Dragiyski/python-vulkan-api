import ctypes

class CType(ctypes.Structure):
    pass

from .VkPresentTimeGOOGLE import CType as VkPresentTimeGOOGLE

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE)),
]
