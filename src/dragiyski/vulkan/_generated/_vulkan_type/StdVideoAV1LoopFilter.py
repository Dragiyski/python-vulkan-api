import ctypes

class StdVideoAV1LoopFilter(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1LoopFilterFlags',
    }
    _included_in_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'loop_filter_level': 'loop_filter_level',
        'loop_filter_sharpness': 'loop_filter_sharpness',
        'update_ref_delta': 'update_ref_delta',
        'loop_filter_ref_deltas': 'loop_filter_ref_deltas',
        'update_mode_delta': 'update_mode_delta',
        'loop_filter_mode_deltas': 'loop_filter_mode_deltas',
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


from .StdVideoAV1LoopFilterFlags import StdVideoAV1LoopFilterFlags

StdVideoAV1LoopFilter._fields_ = [
    ('flags', StdVideoAV1LoopFilterFlags),
    ('loop_filter_level', ctypes.ARRAY(ctypes.c_uint8, 4)),
    ('loop_filter_sharpness', ctypes.c_uint8),
    ('update_ref_delta', ctypes.c_uint8),
    ('loop_filter_ref_deltas', ctypes.ARRAY(ctypes.c_int8, 8)),
    ('update_mode_delta', ctypes.c_uint8),
    ('loop_filter_mode_deltas', ctypes.ARRAY(ctypes.c_int8, 2)),
]

StdVideoAV1LoopFilter._type_ = {
    'flags': StdVideoAV1LoopFilterFlags,
    'loop_filter_level': ctypes.ARRAY(ctypes.c_uint8, 4),
    'loop_filter_sharpness': ctypes.c_uint8,
    'update_ref_delta': ctypes.c_uint8,
    'loop_filter_ref_deltas': ctypes.ARRAY(ctypes.c_int8, 8),
    'update_mode_delta': ctypes.c_uint8,
    'loop_filter_mode_deltas': ctypes.ARRAY(ctypes.c_int8, 2),
}
