import ctypes, sys

class VkPipelineExecutableStatisticKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineExecutableStatisticKHR

from . import VkPipelineExecutableStatisticValueKHR

VkPipelineExecutableStatisticKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('name', ctypes.ARRAY(ctypes.c_char, 256)),
    ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ('format', ctypes.c_int),
    ('value', VkPipelineExecutableStatisticValueKHR),
]
