import ctypes

class VkPipelineViewportWScalingStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'viewportWScalingEnable': ctypes.c_uint32,
            'viewportCount': ctypes.c_uint32,
            'pViewportWScalings': ctypes.POINTER(VkViewportWScalingNV),
        }


from .VkViewportWScalingNV import VkViewportWScalingNV

VkPipelineViewportWScalingStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('viewportWScalingEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportWScalings', ctypes.POINTER(VkViewportWScalingNV)),
]
