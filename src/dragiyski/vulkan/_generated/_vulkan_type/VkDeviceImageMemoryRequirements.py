import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageCreateInfo import CType as VkImageCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkImageCreateInfo)),
    ('planeAspect', ctypes.c_uint32),
]
