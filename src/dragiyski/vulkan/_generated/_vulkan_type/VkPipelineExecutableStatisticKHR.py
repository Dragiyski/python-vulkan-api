import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineExecutableStatisticValueKHR import CType as VkPipelineExecutableStatisticValueKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('name', ctypes.ARRAY(ctypes.c_char, 256)),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('format', ctypes.c_int),
    ('value', VkPipelineExecutableStatisticValueKHR),
]
