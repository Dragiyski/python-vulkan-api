import ctypes

class VkRefreshCycleDurationGOOGLE(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'refreshDuration': ctypes.c_uint64,
        }

    _fields_ = [
        ('refreshDuration', ctypes.c_uint64),
    ]
