import ctypes, sys

class VkVideoDecodeH264CapabilitiesKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeH264CapabilitiesKHR

from . import VkOffset2D

VkVideoDecodeH264CapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxLevelIdc', ctypes.c_int),
    ('fieldOffsetGranularity', VkOffset2D),
]
