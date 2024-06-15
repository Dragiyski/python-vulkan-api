import ctypes, sys

class StdVideoAV1QuantizationFlags(ctypes.Structure):
    _fields_ = [
        ('using_qmatrix', ctypes.c_uint32, 1),
        ('diff_uv_delta', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

sys.modules[__name__] = StdVideoAV1QuantizationFlags
