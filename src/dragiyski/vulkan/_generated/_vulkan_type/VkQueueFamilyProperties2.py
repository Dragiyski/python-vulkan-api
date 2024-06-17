import ctypes, sys

class VkQueueFamilyProperties2(ctypes.Structure):
    pass

sys.modules[__name__] = VkQueueFamilyProperties2

from . import VkQueueFamilyProperties

VkQueueFamilyProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyProperties', VkQueueFamilyProperties),
]
