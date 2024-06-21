import ctypes

class CType(ctypes.Structure):
    pass

from .VkBufferCreateInfo import CType as VkBufferCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pCreateInfo', ctypes.POINTER(VkBufferCreateInfo)),
]
