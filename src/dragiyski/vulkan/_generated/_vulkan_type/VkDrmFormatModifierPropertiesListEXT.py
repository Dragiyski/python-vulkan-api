import ctypes

class VkDrmFormatModifierPropertiesListEXT(ctypes.Structure):
    pass

from .VkDrmFormatModifierPropertiesEXT import VkDrmFormatModifierPropertiesEXT

VkDrmFormatModifierPropertiesListEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierPropertiesEXT)),
]

VkDrmFormatModifierPropertiesListEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifierCount': ctypes.c_uint32,
    'pDrmFormatModifierProperties': ctypes.POINTER(VkDrmFormatModifierPropertiesEXT),
}
