import ctypes

class StdVideoAV1QuantizationFlags(ctypes.Structure):
    _fields_ = [
        ('using_qmatrix', ctypes.c_uint32, 1),
        ('diff_uv_delta', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1Quantization',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'using_qmatrix': 'using_qmatrix',
        'diff_uv_delta': 'diff_uv_delta',
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

StdVideoAV1QuantizationFlags._type_ = {
    'using_qmatrix': ctypes.c_uint32,
    'diff_uv_delta': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
