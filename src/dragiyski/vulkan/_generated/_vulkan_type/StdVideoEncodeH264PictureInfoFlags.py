import ctypes

class StdVideoEncodeH264PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('is_reference', ctypes.c_uint32, 1),
        ('no_output_of_prior_pics_flag', ctypes.c_uint32, 1),
        ('long_term_reference_flag', ctypes.c_uint32, 1),
        ('adaptive_ref_pic_marking_mode_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 27),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH264PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'IdrPicFlag': 'idr_pic_flag',
        'is_reference': 'is_reference',
        'no_output_of_prior_pics_flag': 'no_output_of_prior_pics_flag',
        'long_term_reference_flag': 'long_term_reference_flag',
        'adaptive_ref_pic_marking_mode_flag': 'adaptive_ref_pic_marking_mode_flag',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std_encode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH264PictureInfoFlags._type_ = {
    'IdrPicFlag': ctypes.c_uint32,
    'is_reference': ctypes.c_uint32,
    'no_output_of_prior_pics_flag': ctypes.c_uint32,
    'long_term_reference_flag': ctypes.c_uint32,
    'adaptive_ref_pic_marking_mode_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
