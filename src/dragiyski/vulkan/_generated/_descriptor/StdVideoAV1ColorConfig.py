from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1ColorConfig'
_member_list_ = ['flags', 'BitDepth', 'subsampling_x', 'subsampling_y', 'reserved1', 'color_primaries', 'transfer_characteristics', 'matrix_coefficients', 'chroma_sample_position']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1ColorConfigFlags'),
        'type_name': 'StdVideoAV1ColorConfigFlags',
        'structure': 'StdVideoAV1ColorConfigFlags',
        'is_string': False,
    },
    'BitDepth': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'subsampling_x': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'subsampling_y': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'color_primaries': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1ColorPrimaries',
        'enum': 'StdVideoAV1ColorPrimaries',
        'is_string': False,
    },
    'transfer_characteristics': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1TransferCharacteristics',
        'enum': 'StdVideoAV1TransferCharacteristics',
        'is_string': False,
    },
    'matrix_coefficients': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1MatrixCoefficients',
        'enum': 'StdVideoAV1MatrixCoefficients',
        'is_string': False,
    },
    'chroma_sample_position': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1ChromaSamplePosition',
        'enum': 'StdVideoAV1ChromaSamplePosition',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1ColorConfigFlags',
}
_included_in_ = {
    'StdVideoAV1SequenceHeader',
}
_input_of_ = set()
_output_of_ = set()
