import ctypes

class StdVideoEncodeH265WeightTableFlags(ctypes.Structure):
    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint16),
        ('chroma_weight_l0_flag', ctypes.c_uint16),
        ('luma_weight_l1_flag', ctypes.c_uint16),
        ('chroma_weight_l1_flag', ctypes.c_uint16),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH265WeightTable',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'luma_weight_l0_flag': 'luma_weight_l0_flag',
        'chroma_weight_l0_flag': 'chroma_weight_l0_flag',
        'luma_weight_l1_flag': 'luma_weight_l1_flag',
        'chroma_weight_l1_flag': 'chroma_weight_l1_flag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_encode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH265WeightTableFlags._type_ = {
    'luma_weight_l0_flag': ctypes.c_uint16,
    'chroma_weight_l0_flag': ctypes.c_uint16,
    'luma_weight_l1_flag': ctypes.c_uint16,
    'chroma_weight_l1_flag': ctypes.c_uint16,
}
