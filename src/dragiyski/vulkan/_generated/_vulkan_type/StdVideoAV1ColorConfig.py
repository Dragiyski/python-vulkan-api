import ctypes

class StdVideoAV1ColorConfig(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoAV1ColorConfigFlags,
            'BitDepth': ctypes.c_uint8,
            'subsampling_x': ctypes.c_uint8,
            'subsampling_y': ctypes.c_uint8,
            'reserved1': ctypes.c_uint8,
            'color_primaries': ctypes.c_int,
            'transfer_characteristics': ctypes.c_int,
            'matrix_coefficients': ctypes.c_int,
            'chroma_sample_position': ctypes.c_int,
        }


from .StdVideoAV1ColorConfigFlags import StdVideoAV1ColorConfigFlags

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
