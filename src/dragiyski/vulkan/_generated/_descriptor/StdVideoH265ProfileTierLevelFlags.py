from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265ProfileTierLevelFlags'
_member_list_ = ['general_tier_flag', 'general_progressive_source_flag', 'general_interlaced_source_flag', 'general_non_packed_constraint_flag', 'general_frame_only_constraint_flag']
_member_info_ = {
    'general_tier_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'general_progressive_source_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'general_interlaced_source_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'general_non_packed_constraint_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'general_frame_only_constraint_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265ProfileTierLevel',
}
_input_of_ = set()
_output_of_ = set()
