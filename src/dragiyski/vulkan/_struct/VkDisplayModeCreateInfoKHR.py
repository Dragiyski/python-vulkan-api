import ctypes, sys

class VkDisplayModeCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayModeCreateInfoKHR

from . import VkDisplayModeParametersKHR

VkDisplayModeCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('parameters', VkDisplayModeParametersKHR),
]
