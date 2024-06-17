import ctypes, sys

class VkDisplayPlaneProperties2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayPlaneProperties2KHR

from . import VkDisplayPlanePropertiesKHR

VkDisplayPlaneProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPlaneProperties', VkDisplayPlanePropertiesKHR),
]
