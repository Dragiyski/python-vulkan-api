import ctypes

class CType(ctypes.Structure):
    pass

from .VkRectLayerKHR import CType as VkRectLayerKHR

CType._fields_ = [
    ('rectangleCount', ctypes.c_uint32),
    ('pRectangles', ctypes.POINTER(VkRectLayerKHR)),
]
