import ctypes, sys

class VkSamplerBorderColorComponentMappingCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkSamplerBorderColorComponentMappingCreateInfoEXT

from . import VkComponentMapping

VkSamplerBorderColorComponentMappingCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('components', VkComponentMapping),
    ('srgb', ctypes.c_uint32),
]
