import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkGeneratedCommandsInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'buffer': {'python_name': ['buffer']},
        'offset': {'python_name': ['offset']},
    }
}
