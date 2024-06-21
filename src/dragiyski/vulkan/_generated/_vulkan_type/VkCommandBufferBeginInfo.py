import ctypes

class CType(ctypes.Structure):
    pass

from .VkCommandBufferInheritanceInfo import CType as VkCommandBufferInheritanceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pInheritanceInfo', ctypes.POINTER(VkCommandBufferInheritanceInfo)),
]
