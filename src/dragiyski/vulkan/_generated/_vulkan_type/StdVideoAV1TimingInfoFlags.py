import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('equal_picture_interval', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1TimingInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'equal_picture_interval': {'python_name': ['equal', 'picture', 'interval']},
        'reserved': {'python_name': ['reserved']},
    }
}
