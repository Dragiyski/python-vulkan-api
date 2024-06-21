import ctypes

class CType(ctypes.Structure):
    pass

from .VkDrmFormatModifierPropertiesEXT import CType as VkDrmFormatModifierPropertiesEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierPropertiesEXT)),
]
