import ctypes, sys

class VkMutableDescriptorTypeCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkMutableDescriptorTypeCreateInfoEXT

from . import VkMutableDescriptorTypeListEXT

VkMutableDescriptorTypeCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mutableDescriptorTypeListCount', ctypes.c_uint32),
    ('pMutableDescriptorTypeLists', ctypes.POINTER(VkMutableDescriptorTypeListEXT)),
]
