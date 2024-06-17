import ctypes, sys

class VkPipelineViewportWScalingStateCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineViewportWScalingStateCreateInfoNV

from . import VkViewportWScalingNV

VkPipelineViewportWScalingStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportWScalingEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV)),
]
