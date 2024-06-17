import ctypes, sys

class VkSamplerCustomBorderColorCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkSamplerCustomBorderColorCreateInfoEXT

from . import VkClearColorValue

VkSamplerCustomBorderColorCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('customBorderColor', VkClearColorValue),
    ('format', ctypes.c_int),
]
