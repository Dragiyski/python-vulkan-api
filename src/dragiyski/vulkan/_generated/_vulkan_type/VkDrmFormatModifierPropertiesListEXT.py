import ctypes, sys

class VkDrmFormatModifierPropertiesListEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDrmFormatModifierPropertiesListEXT

from . import VkDrmFormatModifierPropertiesEXT

VkDrmFormatModifierPropertiesListEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierPropertiesEXT)),
]
