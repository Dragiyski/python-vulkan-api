import ctypes, sys

class VkNativeBufferANDROID(ctypes.Structure):
    pass

sys.modules[__name__] = VkNativeBufferANDROID

from . import VkNativeBufferUsage2ANDROID

VkNativeBufferANDROID._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('handle', ctypes.c_void_p),
    ('stride', ctypes.c_int),
    ('format', ctypes.c_int),
    ('usage', ctypes.c_int),
    ('usage2', VkNativeBufferUsage2ANDROID),
]
