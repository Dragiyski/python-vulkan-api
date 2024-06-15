import ctypes, sys

class VkDisplayProperties2KHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayProperties2KHR

from . import VkDisplayPropertiesKHR

VkDisplayProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayProperties', VkDisplayPropertiesKHR),
]
