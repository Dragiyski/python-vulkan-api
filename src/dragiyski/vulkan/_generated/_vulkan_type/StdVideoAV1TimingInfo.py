import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1TimingInfoFlags import CType as StdVideoAV1TimingInfoFlags

CType._fields_ = [
    ('flags', StdVideoAV1TimingInfoFlags),
    ('num_units_in_display_tick', ctypes.c_uint32),
    ('time_scale', ctypes.c_uint32),
    ('num_ticks_per_picture_minus_1', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1TimingInfoFlags',
    },
    'included_in': {
        'StdVideoAV1SequenceHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1TimingInfoFlags'},
        'num_units_in_display_tick': {'python_name': ['num', 'units', 'in', 'display', 'tick']},
        'time_scale': {'python_name': ['time', 'scale']},
        'num_ticks_per_picture_minus_1': {'python_name': ['num', 'ticks', 'per', 'picture', 'minus', '1']},
    }
}
