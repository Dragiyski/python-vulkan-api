import ctypes

class VkPresentTimeGOOGLE(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'presentID': ctypes.c_uint32,
            'desiredPresentTime': ctypes.c_uint64,
        }

    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
    ]
