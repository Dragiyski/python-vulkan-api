import ctypes

class VkCommandBufferInheritanceInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'renderPass': ctypes.c_void_p,
            'subpass': ctypes.c_uint32,
            'framebuffer': ctypes.c_void_p,
            'occlusionQueryEnable': ctypes.c_uint32,
            'queryFlags': ctypes.c_uint32,
            'pipelineStatistics': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('renderPass', ctypes.c_void_p),
        ('subpass', ctypes.c_uint32),
        ('framebuffer', ctypes.c_void_p),
        ('occlusionQueryEnable', ctypes.c_uint32),
        ('queryFlags', ctypes.c_uint32),
        ('pipelineStatistics', ctypes.c_uint32),
    ]
