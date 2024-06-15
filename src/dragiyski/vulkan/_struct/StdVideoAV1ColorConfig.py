import ctypes, sys

class StdVideoAV1ColorConfig(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoAV1ColorConfig

from . import StdVideoAV1ColorConfigFlags

StdVideoAV1ColorConfig._fields_ = [
    ('flags', StdVideoAV1ColorConfigFlags),
    ('BitDepth', ctypes.c_uint8),
    ('subsampling_x', ctypes.c_uint8),
    ('subsampling_y', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('color_primaries', ctypes.c_int),
    ('transfer_characteristics', ctypes.c_int),
    ('matrix_coefficients', ctypes.c_int),
    ('chroma_sample_position', ctypes.c_int),
]
