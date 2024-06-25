import ctypes

class VkSamplerBorderColorComponentMappingCreateInfoEXT(ctypes.Structure):
    pass

from .VkComponentMapping import VkComponentMapping

VkSamplerBorderColorComponentMappingCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('components', VkComponentMapping),
    ('srgb', ctypes.c_uint32),
]

VkSamplerBorderColorComponentMappingCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'components': VkComponentMapping,
    'srgb': ctypes.c_uint32,
}
