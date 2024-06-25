import ctypes

class VkSamplerCustomBorderColorCreateInfoEXT(ctypes.Structure):
    pass

from .VkClearColorValue import VkClearColorValue

VkSamplerCustomBorderColorCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('customBorderColor', VkClearColorValue),
    ('format', ctypes.c_int),
]

VkSamplerCustomBorderColorCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'customBorderColor': VkClearColorValue,
    'format': ctypes.c_int,
}
