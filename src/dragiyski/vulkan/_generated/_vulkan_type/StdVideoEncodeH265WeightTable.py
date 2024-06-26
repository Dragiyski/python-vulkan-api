import ctypes

class StdVideoEncodeH265WeightTable(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoEncodeH265WeightTableFlags',
    }
    _included_in_ = {
        'StdVideoEncodeH265SliceSegmentHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'luma_log2_weight_denom': 'luma_log2_weight_denom',
        'delta_chroma_log2_weight_denom': 'delta_chroma_log2_weight_denom',
        'delta_luma_weight_l0': 'delta_luma_weight_l0',
        'luma_offset_l0': 'luma_offset_l0',
        'delta_chroma_weight_l0': 'delta_chroma_weight_l0',
        'delta_chroma_offset_l0': 'delta_chroma_offset_l0',
        'delta_luma_weight_l1': 'delta_luma_weight_l1',
        'luma_offset_l1': 'luma_offset_l1',
        'delta_chroma_weight_l1': 'delta_chroma_weight_l1',
        'delta_chroma_offset_l1': 'delta_chroma_offset_l1',
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


from .StdVideoEncodeH265WeightTableFlags import StdVideoEncodeH265WeightTableFlags

StdVideoEncodeH265WeightTable._fields_ = [
    ('flags', StdVideoEncodeH265WeightTableFlags),
    ('luma_log2_weight_denom', ctypes.c_uint8),
    ('delta_chroma_log2_weight_denom', ctypes.c_int8),
    ('delta_luma_weight_l0', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('luma_offset_l0', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('delta_chroma_weight_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
    ('delta_chroma_offset_l0', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
    ('delta_luma_weight_l1', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('luma_offset_l1', ctypes.ARRAY(ctypes.c_int8, 15)),
    ('delta_chroma_weight_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
    ('delta_chroma_offset_l1', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15)),
]

StdVideoEncodeH265WeightTable._type_ = {
    'flags': StdVideoEncodeH265WeightTableFlags,
    'luma_log2_weight_denom': ctypes.c_uint8,
    'delta_chroma_log2_weight_denom': ctypes.c_int8,
    'delta_luma_weight_l0': ctypes.ARRAY(ctypes.c_int8, 15),
    'luma_offset_l0': ctypes.ARRAY(ctypes.c_int8, 15),
    'delta_chroma_weight_l0': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
    'delta_chroma_offset_l0': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
    'delta_luma_weight_l1': ctypes.ARRAY(ctypes.c_int8, 15),
    'luma_offset_l1': ctypes.ARRAY(ctypes.c_int8, 15),
    'delta_chroma_weight_l1': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
    'delta_chroma_offset_l1': ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int8, 2), 15),
}
