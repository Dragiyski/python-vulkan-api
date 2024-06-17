import ctypes, sys

class VkDisplayModeProperties2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayModeProperties2KHR

from . import VkDisplayModePropertiesKHR

VkDisplayModeProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayModeProperties', VkDisplayModePropertiesKHR),
]
