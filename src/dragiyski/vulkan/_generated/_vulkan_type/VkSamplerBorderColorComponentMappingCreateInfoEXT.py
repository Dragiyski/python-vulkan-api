import ctypes

class VkSamplerBorderColorComponentMappingCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'components': VkComponentMapping,
            'srgb': ctypes.c_uint32,
        }


from .VkComponentMapping import VkComponentMapping

VkSamplerBorderColorComponentMappingCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('components', VkComponentMapping),
    ('srgb', ctypes.c_uint32),
]
