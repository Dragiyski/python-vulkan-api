import ctypes

class VkVideoEncodeH265SessionParametersFeedbackInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'hasStdVPSOverrides': ctypes.c_uint32,
            'hasStdSPSOverrides': ctypes.c_uint32,
            'hasStdPPSOverrides': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasStdVPSOverrides', ctypes.c_uint32),
        ('hasStdSPSOverrides', ctypes.c_uint32),
        ('hasStdPPSOverrides', ctypes.c_uint32),
    ]
