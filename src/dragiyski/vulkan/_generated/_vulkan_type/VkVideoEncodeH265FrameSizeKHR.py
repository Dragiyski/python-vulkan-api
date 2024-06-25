import ctypes

class VkVideoEncodeH265FrameSizeKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'frameISize': ctypes.c_uint32,
            'framePSize': ctypes.c_uint32,
            'frameBSize': ctypes.c_uint32,
        }

    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]
