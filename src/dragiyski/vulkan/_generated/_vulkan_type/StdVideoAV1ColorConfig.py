import ctypes

class StdVideoAV1ColorConfig(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1ColorConfigFlags',
    }
    _included_in_ = {
        'StdVideoAV1SequenceHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'BitDepth': 'bit_depth',
        'subsampling_x': 'subsampling_x',
        'subsampling_y': 'subsampling_y',
        'reserved1': 'reserved1',
        'color_primaries': 'color_primaries',
        'transfer_characteristics': 'transfer_characteristics',
        'matrix_coefficients': 'matrix_coefficients',
        'chroma_sample_position': 'chroma_sample_position',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = {
        'color_primaries': 'StdVideoAV1ColorPrimaries',
        'transfer_characteristics': 'StdVideoAV1TransferCharacteristics',
        'matrix_coefficients': 'StdVideoAV1MatrixCoefficients',
        'chroma_sample_position': 'StdVideoAV1ChromaSamplePosition',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


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

StdVideoAV1ColorConfig._type_ = {
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
