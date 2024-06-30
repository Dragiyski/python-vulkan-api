from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1CDEF'
_member_list_ = ['cdef_damping_minus_3', 'cdef_bits', 'cdef_y_pri_strength', 'cdef_y_sec_strength', 'cdef_uv_pri_strength', 'cdef_uv_sec_strength']
_member_info_ = {
    'cdef_damping_minus_3': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cdef_bits': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cdef_y_pri_strength': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'cdef_y_sec_strength': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'cdef_uv_pri_strength': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'cdef_uv_sec_strength': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
