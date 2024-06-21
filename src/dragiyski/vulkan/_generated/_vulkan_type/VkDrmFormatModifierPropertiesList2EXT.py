import ctypes

class CType(ctypes.Structure):
    pass

from .VkDrmFormatModifierProperties2EXT import CType as VkDrmFormatModifierProperties2EXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierProperties2EXT)),
]
