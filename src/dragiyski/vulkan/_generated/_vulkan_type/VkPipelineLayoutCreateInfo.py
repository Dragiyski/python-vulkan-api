import ctypes

class CType(ctypes.Structure):
    pass

from .VkPushConstantRange import CType as VkPushConstantRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
]
