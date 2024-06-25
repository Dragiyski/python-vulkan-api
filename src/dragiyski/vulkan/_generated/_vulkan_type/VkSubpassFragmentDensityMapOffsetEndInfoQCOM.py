import ctypes

class VkSubpassFragmentDensityMapOffsetEndInfoQCOM(ctypes.Structure):
    pass

from .VkOffset2D import VkOffset2D

VkSubpassFragmentDensityMapOffsetEndInfoQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetCount', ctypes.c_uint32),
    ('pFragmentDensityOffsets', ctypes.POINTER(VkOffset2D)),
]

VkSubpassFragmentDensityMapOffsetEndInfoQCOM._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fragmentDensityOffsetCount': ctypes.c_uint32,
    'pFragmentDensityOffsets': ctypes.POINTER(VkOffset2D),
}
