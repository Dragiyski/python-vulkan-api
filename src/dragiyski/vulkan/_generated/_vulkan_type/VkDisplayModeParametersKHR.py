import ctypes

class VkDisplayModeParametersKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'visibleRegion': VkExtent2D,
            'refreshRate': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D

VkDisplayModeParametersKHR._fields_ = [
    ('visibleRegion', VkExtent2D),
    ('refreshRate', ctypes.c_uint32),
]
