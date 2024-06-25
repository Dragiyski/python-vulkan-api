import ctypes

class VkImageViewSampleWeightCreateInfoQCOM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'filterCenter': VkOffset2D,
            'filterSize': VkExtent2D,
            'numPhases': ctypes.c_uint32,
        }


from .VkExtent2D import VkExtent2D
from .VkOffset2D import VkOffset2D

VkImageViewSampleWeightCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('filterCenter', VkOffset2D),
    ('filterSize', VkExtent2D),
    ('numPhases', ctypes.c_uint32),
]
