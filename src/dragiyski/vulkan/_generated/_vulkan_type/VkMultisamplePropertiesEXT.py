import ctypes, sys

class VkMultisamplePropertiesEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkMultisamplePropertiesEXT

from . import VkExtent2D

VkMultisamplePropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxSampleLocationGridSize', VkExtent2D),
]
