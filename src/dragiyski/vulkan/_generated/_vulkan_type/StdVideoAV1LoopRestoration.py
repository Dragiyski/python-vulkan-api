import ctypes

class StdVideoAV1LoopRestoration(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'FrameRestorationType': ctypes.ARRAY(ctypes.c_int, 3),
            'LoopRestorationSize': ctypes.ARRAY(ctypes.c_uint16, 3),
        }

    _fields_ = [
        ('FrameRestorationType', ctypes.ARRAY(ctypes.c_int, 3)),
        ('LoopRestorationSize', ctypes.ARRAY(ctypes.c_uint16, 3)),
    ]
