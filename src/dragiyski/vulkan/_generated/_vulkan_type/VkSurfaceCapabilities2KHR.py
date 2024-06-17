import ctypes, sys

class VkSurfaceCapabilities2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkSurfaceCapabilities2KHR

from . import VkSurfaceCapabilitiesKHR

VkSurfaceCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceCapabilities', VkSurfaceCapabilitiesKHR),
]
