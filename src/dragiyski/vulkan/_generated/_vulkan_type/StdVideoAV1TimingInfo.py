import ctypes

class StdVideoAV1TimingInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1TimingInfoFlags',
    }
    _included_in_ = {
        'StdVideoAV1SequenceHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'num_units_in_display_tick': 'num_units_in_display_tick',
        'time_scale': 'time_scale',
        'num_ticks_per_picture_minus_1': 'num_ticks_per_picture_minus_1',
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


from .StdVideoAV1TimingInfoFlags import StdVideoAV1TimingInfoFlags

StdVideoAV1TimingInfo._fields_ = [
    ('flags', StdVideoAV1TimingInfoFlags),
    ('num_units_in_display_tick', ctypes.c_uint32),
    ('time_scale', ctypes.c_uint32),
    ('num_ticks_per_picture_minus_1', ctypes.c_uint32),
]

StdVideoAV1TimingInfo._type_ = {
    'flags': StdVideoAV1TimingInfoFlags,
    'num_units_in_display_tick': ctypes.c_uint32,
    'time_scale': ctypes.c_uint32,
    'num_ticks_per_picture_minus_1': ctypes.c_uint32,
}
