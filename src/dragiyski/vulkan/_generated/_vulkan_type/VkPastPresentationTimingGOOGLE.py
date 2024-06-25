import ctypes

class VkPastPresentationTimingGOOGLE(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'presentID': ctypes.c_uint32,
            'desiredPresentTime': ctypes.c_uint64,
            'actualPresentTime': ctypes.c_uint64,
            'earliestPresentTime': ctypes.c_uint64,
            'presentMargin': ctypes.c_uint64,
        }

    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
        ('actualPresentTime', ctypes.c_uint64),
        ('earliestPresentTime', ctypes.c_uint64),
        ('presentMargin', ctypes.c_uint64),
    ]
