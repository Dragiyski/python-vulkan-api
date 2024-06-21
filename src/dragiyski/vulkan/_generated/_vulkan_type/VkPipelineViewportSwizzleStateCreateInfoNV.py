import ctypes

class CType(ctypes.Structure):
    pass

from .VkViewportSwizzleNV import CType as VkViewportSwizzleNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportSwizzles', ctypes.POINTER(VkViewportSwizzleNV)),
]
