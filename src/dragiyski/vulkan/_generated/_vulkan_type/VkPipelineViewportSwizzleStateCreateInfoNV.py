import ctypes

class VkPipelineViewportSwizzleStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'viewportCount': ctypes.c_uint32,
            'pViewportSwizzles': ctypes.POINTER(VkViewportSwizzleNV),
        }


from .VkViewportSwizzleNV import VkViewportSwizzleNV

VkPipelineViewportSwizzleStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewportSwizzles', ctypes.POINTER(VkViewportSwizzleNV)),
]
