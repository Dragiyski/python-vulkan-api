import ctypes

class StdVideoAV1Quantization(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1QuantizationFlags',
    }
    _included_in_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'base_q_idx': 'base_q_idx',
        'DeltaQYDc': 'delta_qydc',
        'DeltaQUDc': 'delta_qudc',
        'DeltaQUAc': 'delta_quac',
        'DeltaQVDc': 'delta_qvdc',
        'DeltaQVAc': 'delta_qvac',
        'qm_y': 'qm_y',
        'qm_u': 'qm_u',
        'qm_v': 'qm_v',
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


from .StdVideoAV1QuantizationFlags import StdVideoAV1QuantizationFlags

StdVideoAV1Quantization._fields_ = [
    ('flags', StdVideoAV1QuantizationFlags),
    ('base_q_idx', ctypes.c_uint8),
    ('DeltaQYDc', ctypes.c_int8),
    ('DeltaQUDc', ctypes.c_int8),
    ('DeltaQUAc', ctypes.c_int8),
    ('DeltaQVDc', ctypes.c_int8),
    ('DeltaQVAc', ctypes.c_int8),
    ('qm_y', ctypes.c_uint8),
    ('qm_u', ctypes.c_uint8),
    ('qm_v', ctypes.c_uint8),
]

StdVideoAV1Quantization._type_ = {
    'flags': StdVideoAV1QuantizationFlags,
    'base_q_idx': ctypes.c_uint8,
    'DeltaQYDc': ctypes.c_int8,
    'DeltaQUDc': ctypes.c_int8,
    'DeltaQUAc': ctypes.c_int8,
    'DeltaQVDc': ctypes.c_int8,
    'DeltaQVAc': ctypes.c_int8,
    'qm_y': ctypes.c_uint8,
    'qm_u': ctypes.c_uint8,
    'qm_v': ctypes.c_uint8,
}
