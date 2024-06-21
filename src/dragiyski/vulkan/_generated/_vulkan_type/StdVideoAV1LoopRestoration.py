import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('FrameRestorationType', ctypes.ARRAY(ctypes.c_int, 3)),
        ('LoopRestorationSize', ctypes.ARRAY(ctypes.c_uint16, 3)),
    ]
