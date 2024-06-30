from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1ColorConfigFlags'
_member_list_ = ['mono_chrome', 'color_range', 'separate_uv_delta_q', 'color_description_present_flag', 'reserved']
_member_info_ = {
    'mono_chrome': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'color_range': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'separate_uv_delta_q': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'color_description_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 28,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoAV1ColorConfig',
}
_input_of_ = set()
_output_of_ = set()
