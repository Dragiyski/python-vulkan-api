import ctypes

class StdVideoH265ShortTermRefPicSetFlags(ctypes.Structure):
    _fields_ = [
        ('inter_ref_pic_set_prediction_flag', ctypes.c_uint32, 1),
        ('delta_rps_sign', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265ShortTermRefPicSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'inter_ref_pic_set_prediction_flag': 'inter_ref_pic_set_prediction_flag',
        'delta_rps_sign': 'delta_rps_sign',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH265ShortTermRefPicSetFlags._type_ = {
    'inter_ref_pic_set_prediction_flag': ctypes.c_uint32,
    'delta_rps_sign': ctypes.c_uint32,
}
