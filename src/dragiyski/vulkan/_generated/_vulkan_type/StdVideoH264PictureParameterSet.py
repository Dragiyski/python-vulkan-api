import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH264PpsFlags import CType as StdVideoH264PpsFlags
from .StdVideoH264ScalingLists import CType as StdVideoH264ScalingLists

CType._fields_ = [
    ('flags', StdVideoH264PpsFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('num_ref_idx_l0_default_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_default_active_minus1', ctypes.c_uint8),
    ('weighted_bipred_idc', ctypes.c_int),
    ('pic_init_qp_minus26', ctypes.c_int8),
    ('pic_init_qs_minus26', ctypes.c_int8),
    ('chroma_qp_index_offset', ctypes.c_int8),
    ('second_chroma_qp_index_offset', ctypes.c_int8),
    ('pScalingLists', ctypes.POINTER(StdVideoH264ScalingLists)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH264PpsFlags',
        'StdVideoH264ScalingLists',
    },
    'included_in': {
        'VkVideoDecodeH264SessionParametersAddInfoKHR',
        'VkVideoEncodeH264SessionParametersAddInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH264PpsFlags'},
        'seq_parameter_set_id': {'python_name': ['seq', 'parameter', 'set', 'id']},
        'pic_parameter_set_id': {'python_name': ['pic', 'parameter', 'set', 'id']},
        'num_ref_idx_l0_default_active_minus1': {'python_name': ['num', 'ref', 'idx', 'l0', 'default', 'active', 'minus1']},
        'num_ref_idx_l1_default_active_minus1': {'python_name': ['num', 'ref', 'idx', 'l1', 'default', 'active', 'minus1']},
        'weighted_bipred_idc': {'python_name': ['weighted', 'bipred', 'idc'], 'type': 'StdVideoH264WeightedBipredIdc'},
        'pic_init_qp_minus26': {'python_name': ['pic', 'init', 'qp', 'minus26']},
        'pic_init_qs_minus26': {'python_name': ['pic', 'init', 'qs', 'minus26']},
        'chroma_qp_index_offset': {'python_name': ['chroma', 'qp', 'index', 'offset']},
        'second_chroma_qp_index_offset': {'python_name': ['second', 'chroma', 'qp', 'index', 'offset']},
        'pScalingLists': {'python_name': ['p', 'scaling', 'lists'], 'type': 'StdVideoH264ScalingLists'},
    }
}
