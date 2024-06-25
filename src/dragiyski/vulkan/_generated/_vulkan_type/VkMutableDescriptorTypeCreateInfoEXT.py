import ctypes

class VkMutableDescriptorTypeCreateInfoEXT(ctypes.Structure):
    pass

from .VkMutableDescriptorTypeListEXT import VkMutableDescriptorTypeListEXT

VkMutableDescriptorTypeCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mutableDescriptorTypeListCount', ctypes.c_uint32),
    ('pMutableDescriptorTypeLists', ctypes.POINTER(VkMutableDescriptorTypeListEXT)),
]

VkMutableDescriptorTypeCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mutableDescriptorTypeListCount': ctypes.c_uint32,
    'pMutableDescriptorTypeLists': ctypes.POINTER(VkMutableDescriptorTypeListEXT),
}
