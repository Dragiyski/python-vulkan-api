from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264ReferenceInfoFlags'
_member_list_ = ['used_for_long_term_reference', 'reserved']
_member_info_ = {
    'used_for_long_term_reference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 31,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH264ReferenceInfo',
}
_input_of_ = set()
_output_of_ = set()
