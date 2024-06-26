import ctypes

class StdVideoH265LongTermRefPicsSps(ctypes.Structure):
    _fields_ = [
        ('used_by_curr_pic_lt_sps_flag', ctypes.c_uint32),
        ('lt_ref_pic_poc_lsb_sps', ctypes.ARRAY(ctypes.c_uint32, 32)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'used_by_curr_pic_lt_sps_flag': 'used_by_curr_pic_lt_sps_flag',
        'lt_ref_pic_poc_lsb_sps': 'lt_ref_pic_poc_lsb_sps',
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

StdVideoH265LongTermRefPicsSps._type_ = {
    'used_by_curr_pic_lt_sps_flag': ctypes.c_uint32,
    'lt_ref_pic_poc_lsb_sps': ctypes.ARRAY(ctypes.c_uint32, 32),
}
