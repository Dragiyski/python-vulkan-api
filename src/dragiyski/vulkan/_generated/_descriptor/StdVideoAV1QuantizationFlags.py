from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1QuantizationFlags'
_member_list_ = ['using_qmatrix', 'diff_uv_delta', 'reserved']
_member_info_ = {
    'using_qmatrix': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'diff_uv_delta': {
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
    'StdVideoAV1Quantization',
}
_input_of_ = set()
_output_of_ = set()
