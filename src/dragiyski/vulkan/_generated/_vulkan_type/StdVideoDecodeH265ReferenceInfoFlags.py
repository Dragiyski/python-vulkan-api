import ctypes

class StdVideoDecodeH265ReferenceInfoFlags(ctypes.Structure):
    _fields_ = [
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('unused_for_reference', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeH265ReferenceInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'used_for_long_term_reference': 'used_for_long_term_reference',
        'unused_for_reference': 'unused_for_reference',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoDecodeH265ReferenceInfoFlags._type_ = {
    'used_for_long_term_reference': ctypes.c_uint32,
    'unused_for_reference': ctypes.c_uint32,
}
