import ctypes

class VkDrmFormatModifierPropertiesList2EXT(ctypes.Structure):
    pass

from .VkDrmFormatModifierProperties2EXT import VkDrmFormatModifierProperties2EXT

VkDrmFormatModifierPropertiesList2EXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierProperties2EXT)),
]

VkDrmFormatModifierPropertiesList2EXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'drmFormatModifierCount': ctypes.c_uint32,
    'pDrmFormatModifierProperties': ctypes.POINTER(VkDrmFormatModifierProperties2EXT),
}
