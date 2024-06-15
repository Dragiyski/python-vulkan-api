import ctypes, sys

class VkDisplayModePropertiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkDisplayModePropertiesKHR

from . import VkDisplayModeParametersKHR

VkDisplayModePropertiesKHR._fields_ = [
    ('displayMode', ctypes.c_void_p),
    ('parameters', VkDisplayModeParametersKHR),
]
