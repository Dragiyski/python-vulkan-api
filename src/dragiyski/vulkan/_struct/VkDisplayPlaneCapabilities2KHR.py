import ctypes, sys

class VkDisplayPlaneCapabilities2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayPlaneCapabilities2KHR

from . import VkDisplayPlaneCapabilitiesKHR

VkDisplayPlaneCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('capabilities', VkDisplayPlaneCapabilitiesKHR),
]
