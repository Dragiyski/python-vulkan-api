from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH264ReferenceInfoFlags'
_member_list_ = ['top_field_flag', 'bottom_field_flag', 'used_for_long_term_reference', 'is_non_existing']
_member_info_ = {
    'top_field_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'bottom_field_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'used_for_long_term_reference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'is_non_existing': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeH264ReferenceInfo',
}
_input_of_ = set()
_output_of_ = set()
