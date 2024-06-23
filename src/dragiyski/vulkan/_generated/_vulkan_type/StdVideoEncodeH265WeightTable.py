import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265WeightTableFlags import CType as StdVideoEncodeH265WeightTableFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265WeightTableFlags',
    },
    'included_in': {
        'StdVideoEncodeH265SliceSegmentHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH265WeightTableFlags'},
        'luma_log2_weight_denom': {'python_name': ['luma', 'log2', 'weight', 'denom']},
        'delta_chroma_log2_weight_denom': {'python_name': ['delta', 'chroma', 'log2', 'weight', 'denom']},
        'delta_luma_weight_l0': {'python_name': ['delta', 'luma', 'weight', 'l0']},
        'luma_offset_l0': {'python_name': ['luma', 'offset', 'l0']},
        'delta_chroma_weight_l0': {'python_name': ['delta', 'chroma', 'weight', 'l0']},
        'delta_chroma_offset_l0': {'python_name': ['delta', 'chroma', 'offset', 'l0']},
        'delta_luma_weight_l1': {'python_name': ['delta', 'luma', 'weight', 'l1']},
        'luma_offset_l1': {'python_name': ['luma', 'offset', 'l1']},
        'delta_chroma_weight_l1': {'python_name': ['delta', 'chroma', 'weight', 'l1']},
        'delta_chroma_offset_l1': {'python_name': ['delta', 'chroma', 'offset', 'l1']},
    }
}
