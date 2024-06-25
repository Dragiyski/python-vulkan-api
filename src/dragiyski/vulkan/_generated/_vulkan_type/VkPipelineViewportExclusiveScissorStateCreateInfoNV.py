import ctypes

class VkPipelineViewportExclusiveScissorStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'exclusiveScissorCount': ctypes.c_uint32,
            'pExclusiveScissors': ctypes.POINTER(VkRect2D),
        }


from .VkRect2D import VkRect2D

VkPipelineViewportExclusiveScissorStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('exclusiveScissorCount', ctypes.c_uint32),
    ('pExclusiveScissors', ctypes.POINTER(VkRect2D)),
]
