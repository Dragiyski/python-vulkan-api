import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
        ('actualPresentTime', ctypes.c_uint64),
        ('earliestPresentTime', ctypes.c_uint64),
        ('presentMargin', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPastPresentationTimingGOOGLE',
    },
    'member_map': {
        'presentID': {'python_name': ['present', 'id']},
        'desiredPresentTime': {'python_name': ['desired', 'present', 'time']},
        'actualPresentTime': {'python_name': ['actual', 'present', 'time']},
        'earliestPresentTime': {'python_name': ['earliest', 'present', 'time']},
        'presentMargin': {'python_name': ['present', 'margin']},
    }
}
