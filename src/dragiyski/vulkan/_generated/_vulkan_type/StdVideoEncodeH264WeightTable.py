import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264WeightTableFlags import CType as StdVideoEncodeH264WeightTableFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264WeightTableFlags',
    },
    'included_in': {
        'StdVideoEncodeH264SliceHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH264WeightTableFlags'},
        'luma_log2_weight_denom': {'python_name': ['luma', 'log2', 'weight', 'denom']},
        'chroma_log2_weight_denom': {'python_name': ['chroma', 'log2', 'weight', 'denom']},
        'luma_weight_l0': {'python_name': ['luma', 'weight', 'l0']},
        'luma_offset_l0': {'python_name': ['luma', 'offset', 'l0']},
        'chroma_weight_l0': {'python_name': ['chroma', 'weight', 'l0']},
        'chroma_offset_l0': {'python_name': ['chroma', 'offset', 'l0']},
        'luma_weight_l1': {'python_name': ['luma', 'weight', 'l1']},
        'luma_offset_l1': {'python_name': ['luma', 'offset', 'l1']},
        'chroma_weight_l1': {'python_name': ['chroma', 'weight', 'l1']},
        'chroma_offset_l1': {'python_name': ['chroma', 'offset', 'l1']},
    }
}
