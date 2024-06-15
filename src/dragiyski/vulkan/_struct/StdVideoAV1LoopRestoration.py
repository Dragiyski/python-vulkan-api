import ctypes, sys

class StdVideoAV1LoopRestoration(ctypes.Structure):
    _fields_ = [
        ('FrameRestorationType', ctypes.ARRAY(ctypes.c_int, 3)),
        ('LoopRestorationSize', ctypes.ARRAY(ctypes.c_uint16, 3)),
    ]

sys.modules[__name__] = StdVideoAV1LoopRestoration
