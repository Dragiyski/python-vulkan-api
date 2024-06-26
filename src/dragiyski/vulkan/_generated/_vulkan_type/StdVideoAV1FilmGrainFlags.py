import ctypes

class StdVideoAV1FilmGrainFlags(ctypes.Structure):
    _fields_ = [
        ('chroma_scaling_from_luma', ctypes.c_uint32, 1),
        ('overlap_flag', ctypes.c_uint32, 1),
        ('clip_to_restricted_range', ctypes.c_uint32, 1),
        ('update_grain', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1FilmGrain',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'chroma_scaling_from_luma': 'chroma_scaling_from_luma',
        'overlap_flag': 'overlap_flag',
        'clip_to_restricted_range': 'clip_to_restricted_range',
        'update_grain': 'update_grain',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoAV1FilmGrainFlags._type_ = {
    'chroma_scaling_from_luma': ctypes.c_uint32,
    'overlap_flag': ctypes.c_uint32,
    'clip_to_restricted_range': ctypes.c_uint32,
    'update_grain': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
