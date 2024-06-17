import ctypes, sys

class VkPhysicalDeviceProperties2(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceProperties2

from . import VkPhysicalDeviceProperties

VkPhysicalDeviceProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkPhysicalDeviceProperties),
]
