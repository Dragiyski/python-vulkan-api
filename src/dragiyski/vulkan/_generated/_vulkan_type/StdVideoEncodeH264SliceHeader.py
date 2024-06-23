import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264SliceHeaderFlags import CType as StdVideoEncodeH264SliceHeaderFlags
from .StdVideoEncodeH264WeightTable import CType as StdVideoEncodeH264WeightTable

CType._fields_ = [
    ('flags', StdVideoEncodeH264SliceHeaderFlags),
    ('first_mb_in_slice', ctypes.c_uint32),
    ('slice_type', ctypes.c_int),
    ('slice_alpha_c0_offset_div2', ctypes.c_int8),
    ('slice_beta_offset_div2', ctypes.c_int8),
    ('slice_qp_delta', ctypes.c_int8),
    ('reserved1', ctypes.c_uint8),
    ('cabac_init_idc', ctypes.c_int),
    ('disable_deblocking_filter_idc', ctypes.c_int),
    ('pWeightTable', ctypes.POINTER(StdVideoEncodeH264WeightTable)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264SliceHeaderFlags',
        'StdVideoEncodeH264WeightTable',
    },
    'included_in': {
        'VkVideoEncodeH264NaluSliceInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH264SliceHeaderFlags'},
        'first_mb_in_slice': {'python_name': ['first', 'mb', 'in', 'slice']},
        'slice_type': {'python_name': ['slice', 'type'], 'type': 'StdVideoH264SliceType'},
        'slice_alpha_c0_offset_div2': {'python_name': ['slice', 'alpha', 'c0', 'offset', 'div2']},
        'slice_beta_offset_div2': {'python_name': ['slice', 'beta', 'offset', 'div2']},
        'slice_qp_delta': {'python_name': ['slice', 'qp', 'delta']},
        'reserved1': {'python_name': ['reserved1']},
        'cabac_init_idc': {'python_name': ['cabac', 'init', 'idc'], 'type': 'StdVideoH264CabacInitIdc'},
        'disable_deblocking_filter_idc': {'python_name': ['disable', 'deblocking', 'filter', 'idc'], 'type': 'StdVideoH264DisableDeblockingFilterIdc'},
        'pWeightTable': {'python_name': ['p', 'weight', 'table'], 'type': 'StdVideoEncodeH264WeightTable'},
    }
}
