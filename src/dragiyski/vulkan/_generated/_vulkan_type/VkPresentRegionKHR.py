import ctypes

class VkPresentRegionKHR(ctypes.Structure):
    pass

from .VkRectLayerKHR import VkRectLayerKHR

VkPresentRegionKHR._fields_ = [
    ('rectangleCount', ctypes.c_uint32),
    ('pRectangles', ctypes.POINTER(VkRectLayerKHR)),
]

VkPresentRegionKHR._type_ = {
    'rectangleCount': ctypes.c_uint32,
    'pRectangles': ctypes.POINTER(VkRectLayerKHR),
}
