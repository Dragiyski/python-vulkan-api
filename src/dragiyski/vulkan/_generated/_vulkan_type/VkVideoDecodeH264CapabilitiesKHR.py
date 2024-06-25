import ctypes

class VkVideoDecodeH264CapabilitiesKHR(ctypes.Structure):
    pass

from .VkOffset2D import VkOffset2D

VkVideoDecodeH264CapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxLevelIdc', ctypes.c_int),
    ('fieldOffsetGranularity', VkOffset2D),
]

VkVideoDecodeH264CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxLevelIdc': ctypes.c_int,
    'fieldOffsetGranularity': VkOffset2D,
}
