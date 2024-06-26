import ctypes

class StdVideoAV1ColorConfigFlags(ctypes.Structure):
    _fields_ = [
        ('mono_chrome', ctypes.c_uint32, 1),
        ('color_range', ctypes.c_uint32, 1),
        ('separate_uv_delta_q', ctypes.c_uint32, 1),
        ('color_description_present_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1ColorConfig',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'mono_chrome': 'mono_chrome',
        'color_range': 'color_range',
        'separate_uv_delta_q': 'separate_uv_delta_q',
        'color_description_present_flag': 'color_description_present_flag',
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

StdVideoAV1ColorConfigFlags._type_ = {
    'mono_chrome': ctypes.c_uint32,
    'color_range': ctypes.c_uint32,
    'separate_uv_delta_q': ctypes.c_uint32,
    'color_description_present_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
