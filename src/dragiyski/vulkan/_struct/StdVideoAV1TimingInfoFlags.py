import ctypes, sys

class StdVideoAV1TimingInfoFlags(ctypes.Structure):
    _fields_ = [
        ('equal_picture_interval', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

sys.modules[__name__] = StdVideoAV1TimingInfoFlags
