import ctypes

class StdVideoAV1TimingInfoFlags(ctypes.Structure):
    _fields_ = [
        ('equal_picture_interval', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

StdVideoAV1TimingInfoFlags._type_ = {
    'equal_picture_interval': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
