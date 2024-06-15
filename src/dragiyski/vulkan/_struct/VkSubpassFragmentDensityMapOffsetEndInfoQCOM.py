import ctypes, sys

class VkSubpassFragmentDensityMapOffsetEndInfoQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkSubpassFragmentDensityMapOffsetEndInfoQCOM

from . import VkOffset2D

VkSubpassFragmentDensityMapOffsetEndInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetCount', ctypes.c_uint32),
    ('pFragmentDensityOffsets', ctypes.POINTER(VkOffset2D)),
]
