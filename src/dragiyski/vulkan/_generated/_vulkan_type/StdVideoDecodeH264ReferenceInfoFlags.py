import ctypes

class StdVideoDecodeH264ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('top_field_flag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('is_non_existing', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeH264ReferenceInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'top_field_flag': 'top_field_flag',
        'bottom_field_flag': 'bottom_field_flag',
        'used_for_long_term_reference': 'used_for_long_term_reference',
        'is_non_existing': 'is_non_existing',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoDecodeH264ReferenceInfoFlags._type_ = {
    'top_field_flag': ctypes.c_uint32,
    'bottom_field_flag': ctypes.c_uint32,
    'used_for_long_term_reference': ctypes.c_uint32,
    'is_non_existing': ctypes.c_uint32,
}
