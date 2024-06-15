import ctypes, sys

class VkSurfaceFormat2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkSurfaceFormat2KHR

from . import VkSurfaceFormatKHR

VkSurfaceFormat2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceFormat', VkSurfaceFormatKHR),
]
