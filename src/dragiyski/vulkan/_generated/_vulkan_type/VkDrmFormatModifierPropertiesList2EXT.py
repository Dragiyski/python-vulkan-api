import ctypes, sys

class VkDrmFormatModifierPropertiesList2EXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDrmFormatModifierPropertiesList2EXT

from . import VkDrmFormatModifierProperties2EXT

VkDrmFormatModifierPropertiesList2EXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierProperties2EXT)),
]
