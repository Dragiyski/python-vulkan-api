import ctypes

class VkPipelineViewportWScalingStateCreateInfoNV(ctypes.Structure):
    pass

from .VkViewportWScalingNV import VkViewportWScalingNV

VkPipelineViewportWScalingStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportWScalingEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV)),
]

VkPipelineViewportWScalingStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'viewportWScalingEnable': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pViewportWScalings': ctypes.POINTER(VkViewportWScalingNV),
}
