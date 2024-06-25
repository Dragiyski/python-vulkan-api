import ctypes

class VkVideoEncodeH265GopRemainingFrameInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'useGopRemainingFrames': ctypes.c_uint32,
            'gopRemainingI': ctypes.c_uint32,
            'gopRemainingP': ctypes.c_uint32,
            'gopRemainingB': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useGopRemainingFrames', ctypes.c_uint32),
        ('gopRemainingI', ctypes.c_uint32),
        ('gopRemainingP', ctypes.c_uint32),
        ('gopRemainingB', ctypes.c_uint32),
    ]
