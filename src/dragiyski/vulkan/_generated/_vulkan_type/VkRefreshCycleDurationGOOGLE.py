import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('refreshDuration', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetRefreshCycleDurationGOOGLE',
    },
    'member_map': {
        'refreshDuration': {'python_name': ['refresh', 'duration']},
    }
}
