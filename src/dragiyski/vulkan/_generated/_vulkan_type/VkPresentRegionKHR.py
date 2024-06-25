import ctypes

class VkPresentRegionKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'rectangleCount': ctypes.c_uint32,
            'pRectangles': ctypes.POINTER(VkRectLayerKHR),
        }


from .VkRectLayerKHR import VkRectLayerKHR

VkPresentRegionKHR._fields_ = [
    ('rectangleCount', ctypes.c_uint32),
    ('pRectangles', ctypes.POINTER(VkRectLayerKHR)),
]
