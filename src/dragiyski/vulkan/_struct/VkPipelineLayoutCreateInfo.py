import ctypes, sys

class VkPipelineLayoutCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineLayoutCreateInfo

from . import VkPushConstantRange

VkPipelineLayoutCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
]
