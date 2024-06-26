import ctypes

class StdVideoDecodeH265PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('IsReference', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeH265PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'IrapPicFlag': 'irap_pic_flag',
        'IdrPicFlag': 'idr_pic_flag',
        'IsReference': 'is_reference',
        'short_term_ref_pic_set_sps_flag': 'short_term_ref_pic_set_sps_flag',
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

StdVideoDecodeH265PictureInfoFlags._type_ = {
    'IrapPicFlag': ctypes.c_uint32,
    'IdrPicFlag': ctypes.c_uint32,
    'IsReference': ctypes.c_uint32,
    'short_term_ref_pic_set_sps_flag': ctypes.c_uint32,
}
