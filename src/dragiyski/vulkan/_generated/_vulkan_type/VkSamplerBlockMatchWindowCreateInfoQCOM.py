import ctypes

class VkSamplerBlockMatchWindowCreateInfoQCOM(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkSamplerBlockMatchWindowCreateInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('windowExtent', VkExtent2D),
    ('windowCompareMode', ctypes.c_int),
]

VkSamplerBlockMatchWindowCreateInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'windowExtent': VkExtent2D,
    'windowCompareMode': ctypes.c_int,
}
