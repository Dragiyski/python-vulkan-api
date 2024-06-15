import ctypes, sys

class VkPresentRegionKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPresentRegionKHR

from . import VkRectLayerKHR

VkPresentRegionKHR._fields_ = [
    ('rectangleCount', ctypes.c_uint32),
    ('pRectangles', ctypes.POINTER(VkRectLayerKHR)),
]
