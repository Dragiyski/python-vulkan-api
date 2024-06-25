import ctypes

class StdVideoAV1ColorConfigFlags(ctypes.Structure):
    _fields_ = [
        ('mono_chrome', ctypes.c_uint32, 1),
        ('color_range', ctypes.c_uint32, 1),
        ('separate_uv_delta_q', ctypes.c_uint32, 1),
        ('color_description_present_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]

StdVideoAV1ColorConfigFlags._type_ = {
    'mono_chrome': ctypes.c_uint32,
    'color_range': ctypes.c_uint32,
    'separate_uv_delta_q': ctypes.c_uint32,
    'color_description_present_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
