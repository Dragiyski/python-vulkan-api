import ctypes

class VkSamplerCustomBorderColorCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'customBorderColor': VkClearColorValue,
            'format': ctypes.c_int,
        }


from .VkClearColorValue import VkClearColorValue

VkSamplerCustomBorderColorCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('customBorderColor', VkClearColorValue),
    ('format', ctypes.c_int),
]
