import ctypes

class VkDescriptorGetInfoEXT(ctypes.Structure):
    pass

from .VkDescriptorDataEXT import VkDescriptorDataEXT

VkDescriptorGetInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('data', VkDescriptorDataEXT),
]

VkDescriptorGetInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'data': VkDescriptorDataEXT,
}
