import ctypes

class CType(ctypes.Structure):
    pass

from .VkViewportWScalingNV import CType as VkViewportWScalingNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportWScalingEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV)),
]
