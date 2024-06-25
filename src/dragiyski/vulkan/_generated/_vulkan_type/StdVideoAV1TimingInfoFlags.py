import ctypes

class StdVideoAV1TimingInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'equal_picture_interval': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('equal_picture_interval', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]
