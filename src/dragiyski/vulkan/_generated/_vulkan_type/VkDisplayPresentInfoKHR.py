import ctypes, sys

class VkDisplayPresentInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayPresentInfoKHR

from . import VkRect2D

VkDisplayPresentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('srcRect', VkRect2D),
    ('dstRect', VkRect2D),
    ('persistent', ctypes.c_uint32),
]
