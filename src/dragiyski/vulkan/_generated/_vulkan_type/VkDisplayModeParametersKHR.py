import ctypes

class VkDisplayModeParametersKHR(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkDisplayModeParametersKHR._fields_ = [
    ('visibleRegion', VkExtent2D),
    ('refreshRate', ctypes.c_uint32),
]

VkDisplayModeParametersKHR._type_ = {
    'visibleRegion': VkExtent2D,
    'refreshRate': ctypes.c_uint32,
}
