import ctypes, sys

class VkDescriptorGetInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDescriptorGetInfoEXT

from . import VkDescriptorDataEXT

VkDescriptorGetInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('data', VkDescriptorDataEXT),
]
