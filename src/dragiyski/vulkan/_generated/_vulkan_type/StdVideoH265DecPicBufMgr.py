import ctypes

class StdVideoH265DecPicBufMgr(ctypes.Structure):
    _fields_ = [
        ('max_latency_increase_plus1', ctypes.ARRAY(ctypes.c_uint32, 7)),
        ('max_dec_pic_buffering_minus1', ctypes.ARRAY(ctypes.c_uint8, 7)),
        ('max_num_reorder_pics', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265SequenceParameterSet',
        'StdVideoH265VideoParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'max_latency_increase_plus1': 'max_latency_increase_plus1',
        'max_dec_pic_buffering_minus1': 'max_dec_pic_buffering_minus1',
        'max_num_reorder_pics': 'max_num_reorder_pics',
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

StdVideoH265DecPicBufMgr._type_ = {
    'max_latency_increase_plus1': ctypes.ARRAY(ctypes.c_uint32, 7),
    'max_dec_pic_buffering_minus1': ctypes.ARRAY(ctypes.c_uint8, 7),
    'max_num_reorder_pics': ctypes.ARRAY(ctypes.c_uint8, 7),
}
