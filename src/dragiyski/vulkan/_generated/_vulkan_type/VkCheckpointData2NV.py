import ctypes

class VkCheckpointData2NV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stage': ctypes.c_uint64,
            'pCheckpointMarker': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stage', ctypes.c_uint64),
        ('pCheckpointMarker', ctypes.c_void_p),
    ]
