from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1FilmGrainFlags'
_member_list_ = ['chroma_scaling_from_luma', 'overlap_flag', 'clip_to_restricted_range', 'update_grain', 'reserved']
_member_info_ = {
    'chroma_scaling_from_luma': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'overlap_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'clip_to_restricted_range': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'update_grain': {
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
    'StdVideoAV1FilmGrain',
}
_input_of_ = set()
_output_of_ = set()
