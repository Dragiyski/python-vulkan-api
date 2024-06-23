import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPresentTimesInfoGOOGLE',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'presentID': {'python_name': ['present', 'id']},
        'desiredPresentTime': {'python_name': ['desired', 'present', 'time']},
    }
}
