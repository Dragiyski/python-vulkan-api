import ctypes

class CType(ctypes.Structure):
    pass

from .VkMutableDescriptorTypeListEXT import CType as VkMutableDescriptorTypeListEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mutableDescriptorTypeListCount', ctypes.c_uint32),
    ('pMutableDescriptorTypeLists', ctypes.POINTER(VkMutableDescriptorTypeListEXT)),
]
