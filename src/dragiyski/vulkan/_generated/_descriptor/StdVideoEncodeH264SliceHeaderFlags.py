from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264SliceHeaderFlags'
_member_list_ = ['direct_spatial_mv_pred_flag', 'num_ref_idx_active_override_flag', 'reserved']
_member_info_ = {
    'direct_spatial_mv_pred_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'num_ref_idx_active_override_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 30,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH264SliceHeader',
}
_input_of_ = set()
_output_of_ = set()
