from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1SequenceHeader'
_member_list_ = ['flags', 'seq_profile', 'frame_width_bits_minus_1', 'frame_height_bits_minus_1', 'max_frame_width_minus_1', 'max_frame_height_minus_1', 'delta_frame_id_length_minus_2', 'additional_frame_id_length_minus_1', 'order_hint_bits_minus_1', 'seq_force_integer_mv', 'seq_force_screen_content_tools', 'reserved1', 'pColorConfig', 'pTimingInfo']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1SequenceHeaderFlags'),
        'type_name': 'StdVideoAV1SequenceHeaderFlags',
        'structure': 'StdVideoAV1SequenceHeaderFlags',
        'is_string': False,
    },
    'seq_profile': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1Profile',
        'enum': 'StdVideoAV1Profile',
        'is_string': False,
    },
    'frame_width_bits_minus_1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'frame_height_bits_minus_1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'max_frame_width_minus_1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'max_frame_height_minus_1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'delta_frame_id_length_minus_2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'additional_frame_id_length_minus_1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'order_hint_bits_minus_1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'seq_force_integer_mv': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'seq_force_screen_content_tools': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CArrayType(CIntType('c_uint8'), 5),
        'is_string': False,
    },
    'pColorConfig': {
        'type': CPointerType(CComplexType('StdVideoAV1ColorConfig')),
        'type_name': 'StdVideoAV1ColorConfig',
        'structure': 'StdVideoAV1ColorConfig',
        'is_string': False,
    },
    'pTimingInfo': {
        'type': CPointerType(CComplexType('StdVideoAV1TimingInfo')),
        'type_name': 'StdVideoAV1TimingInfo',
        'structure': 'StdVideoAV1TimingInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1ColorConfig',
    'StdVideoAV1SequenceHeaderFlags',
    'StdVideoAV1TimingInfo',
}
_included_in_ = {
    'VkVideoDecodeAV1SessionParametersCreateInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
