import ctypes

class StdVideoAV1QuantizationFlags(ctypes.Structure):
    _fields_ = [
        ('using_qmatrix', ctypes.c_uint32, 1),
        ('diff_uv_delta', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

StdVideoAV1QuantizationFlags._type_ = {
    'using_qmatrix': ctypes.c_uint32,
    'diff_uv_delta': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
