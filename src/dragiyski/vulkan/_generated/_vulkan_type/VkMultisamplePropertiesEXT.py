import ctypes

class VkMultisamplePropertiesEXT(ctypes.Structure):
    pass

from .VkExtent2D import VkExtent2D

VkMultisamplePropertiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxSampleLocationGridSize', VkExtent2D),
]

VkMultisamplePropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxSampleLocationGridSize': VkExtent2D,
}
