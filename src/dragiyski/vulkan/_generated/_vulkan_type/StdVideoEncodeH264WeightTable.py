import ctypes

class StdVideoEncodeH264WeightTable(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH264WeightTableFlags',
    }
    _included_in_ = {
        'StdVideoEncodeH264SliceHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'luma_log2_weight_denom': 'luma_log2_weight_denom',
        'chroma_log2_weight_denom': 'chroma_log2_weight_denom',
        'luma_weight_l0': 'luma_weight_l0',
        'luma_offset_l0': 'luma_offset_l0',
        'chroma_weight_l0': 'chroma_weight_l0',
        'chroma_offset_l0': 'chroma_offset_l0',
        'luma_weight_l1': 'luma_weight_l1',
        'luma_offset_l1': 'luma_offset_l1',
        'chroma_weight_l1': 'chroma_weight_l1',
        'chroma_offset_l1': 'chroma_offset_l1',
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


from .StdVideoEncodeH264WeightTableFlags import StdVideoEncodeH264WeightTableFlags

StdVideoEncodeH264WeightTable._fields_ = [
    ('flags', StdVideoEncodeH264WeightTableFlags),
    ('luma_log2_weight_denom', ctypes.c_uint8),
    ('chroma_log2_weight_denom', ctypes.c_uint8),
    ('luma_weight_l0', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('luma_offset_l0', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('chroma_weight_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
    ('chroma_offset_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
    ('luma_weight_l1', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('luma_offset_l1', ctypes.ARRAY(ctypes.c_int8, 32)),
    ('chroma_weight_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
    ('chroma_offset_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32)),
]

StdVideoEncodeH264WeightTable._type_ = {
    'flags': StdVideoEncodeH264WeightTableFlags,
    'luma_log2_weight_denom': ctypes.c_uint8,
    'chroma_log2_weight_denom': ctypes.c_uint8,
    'luma_weight_l0': ctypes.ARRAY(ctypes.c_int8, 32),
    'luma_offset_l0': ctypes.ARRAY(ctypes.c_int8, 32),
    'chroma_weight_l0': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32),
    'chroma_offset_l0': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32),
    'luma_weight_l1': ctypes.ARRAY(ctypes.c_int8, 32),
    'luma_offset_l1': ctypes.ARRAY(ctypes.c_int8, 32),
    'chroma_weight_l1': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32),
    'chroma_offset_l1': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 32),
}
