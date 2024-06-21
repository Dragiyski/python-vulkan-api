import ctypes

class CType(ctypes.Structure):
    pass

from .VkNativeBufferUsage2ANDROID import CType as VkNativeBufferUsage2ANDROID

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('handle', ctypes.c_void_p),
    ('stride', ctypes.c_int),
    ('format', ctypes.c_int),
    ('usage', ctypes.c_int),
    ('usage2', VkNativeBufferUsage2ANDROID),
]
