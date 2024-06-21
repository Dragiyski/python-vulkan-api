import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorDataEXT import CType as VkDescriptorDataEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('data', VkDescriptorDataEXT),
]
