import ctypes, sys

class VkSamplerBlockMatchWindowCreateInfoQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkSamplerBlockMatchWindowCreateInfoQCOM

from . import VkExtent2D

VkSamplerBlockMatchWindowCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('windowExtent', VkExtent2D),
    ('windowCompareMode', ctypes.c_int),
]
