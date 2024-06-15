import ctypes, sys

class VkDisplayModeParametersKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayModeParametersKHR

from . import VkExtent2D

VkDisplayModeParametersKHR._fields_ = [
    ('visibleRegion', VkExtent2D),
    ('refreshRate', ctypes.c_uint32),
]
