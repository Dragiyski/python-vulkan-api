import ctypes

class StdVideoAV1LoopFilterFlags(ctypes.Structure):
    _fields_ = [
        ('loop_filter_delta_enabled', ctypes.c_uint32, 1),
        ('loop_filter_delta_update', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1LoopFilter',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'loop_filter_delta_enabled': 'loop_filter_delta_enabled',
        'loop_filter_delta_update': 'loop_filter_delta_update',
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

StdVideoAV1LoopFilterFlags._type_ = {
    'loop_filter_delta_enabled': ctypes.c_uint32,
    'loop_filter_delta_update': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
