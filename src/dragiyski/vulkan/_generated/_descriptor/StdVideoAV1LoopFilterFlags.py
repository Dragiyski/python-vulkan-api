from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1LoopFilterFlags'
_member_list_ = ['loop_filter_delta_enabled', 'loop_filter_delta_update', 'reserved']
_member_info_ = {
    'loop_filter_delta_enabled': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'loop_filter_delta_update': {
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
    'StdVideoAV1LoopFilter',
}
_input_of_ = set()
_output_of_ = set()
