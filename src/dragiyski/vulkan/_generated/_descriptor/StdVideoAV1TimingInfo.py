from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1TimingInfo'
_member_list_ = ['flags', 'num_units_in_display_tick', 'time_scale', 'num_ticks_per_picture_minus_1']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1TimingInfoFlags'),
        'type_name': 'StdVideoAV1TimingInfoFlags',
        'structure': 'StdVideoAV1TimingInfoFlags',
        'is_string': False,
    },
    'num_units_in_display_tick': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'time_scale': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'num_ticks_per_picture_minus_1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1TimingInfoFlags',
}
_included_in_ = {
    'StdVideoAV1SequenceHeader',
}
_input_of_ = set()
_output_of_ = set()
