import ctypes

class StdVideoDecodeH264PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('field_pic_flag', ctypes.c_uint32, 1),
        ('is_intra', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('bottom_field_flag', ctypes.c_uint32, 1),
        ('is_reference', ctypes.c_uint32, 1),
        ('complementary_field_pair', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeH264PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'field_pic_flag': 'field_pic_flag',
        'is_intra': 'is_intra',
        'IdrPicFlag': 'idr_pic_flag',
        'bottom_field_flag': 'bottom_field_flag',
        'is_reference': 'is_reference',
        'complementary_field_pair': 'complementary_field_pair',
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

StdVideoDecodeH264PictureInfoFlags._type_ = {
    'field_pic_flag': ctypes.c_uint32,
    'is_intra': ctypes.c_uint32,
    'IdrPicFlag': ctypes.c_uint32,
    'bottom_field_flag': ctypes.c_uint32,
    'is_reference': ctypes.c_uint32,
    'complementary_field_pair': ctypes.c_uint32,
}
