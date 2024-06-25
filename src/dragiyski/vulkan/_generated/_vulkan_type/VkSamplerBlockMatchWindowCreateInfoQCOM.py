import ctypes

class VkSamplerBlockMatchWindowCreateInfoQCOM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'windowExtent': VkExtent2D,
            'windowCompareMode': ctypes.c_int,
        }


from .VkExtent2D import VkExtent2D

VkSamplerBlockMatchWindowCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('windowExtent', VkExtent2D),
    ('windowCompareMode', ctypes.c_int),
]
